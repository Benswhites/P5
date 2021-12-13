#!/usr/bin/env python
from actionlib.action_server import ros_timer
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import threading

process_units = [["red", "idle", -1.5, 0.0], ["green", "idle", -1.0, 0.0], ["blue", "idle", -0.5, 0.0],["drop_off", "idle", 1.0, 0.0],["home1", "idle", 1.0, -1.0]]
product_units = [["Bot1", "idle"]]
tasks = []
tasks.append([["red", "pending", 3],["green", "pending", 2],["drop_off", "pending", 1],["home1", "pending", 1]])

order = 0

rospy.init_node('movebase_client', anonymous=True)

def make_robot(x, y, robot): # Should be called move_robot.
    client = actionlib.SimpleActionClient(robot + '/move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = 1.0 # Not just = w?

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    #     rospy.loginfo(client.get_result()) # This line is redundant. As such, it needs to be commented out.

    # else:
    #     rospy.loginfo(client.get_result())
    
    return client.get_result

def task_received(task, unit):
    location = [0, 0] # Please explain. Is this simply (x,y)
    job = len(task)
    while job > 0:
        for j in range(len(task)):
            for i in range(len(process_units)):
                test = task[j][0] in process_units[i] # We need better name than "test".
                if test == True and process_units[i][1] == "idle" and task[j][1] == "pending":
                    location[0] = process_units[i][2] # This is not very general is it?
                    location[1] = process_units[i][3]
                    done = "no"
                    while done == "no":
                        done = make_robot(location[0], location[1], unit[0])
                        job -= 1
                        task[j][1] = "complete"
    rospy.loginfo(unit[0] + ": goal complete")
    unit[1] = "idle"
    return "idle"

while order < len(tasks):
    #for i in range(len(tasks)): # was process unit. oops haha.
    for i in range(len(product_units)): # was process unit. oops haha. # Det er muligt at det er linjen over der virker.

        if product_units[i][1] == "idle":
            product_units[i][1] = "active"
            threading.Thread(target=task_received, args=(tasks[order], product_units[i])).start()
            order += 1
        if len(tasks) == 0:
            break