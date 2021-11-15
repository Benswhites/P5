#!/usr/bin/env python

## **Imports**
import sys
import time

import rospy
import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseActionResult, MoveBaseActionGoal
from geometry_msgs.msg import Pose, Point, Quaternion


## **Functions**
def callback_movebase_result(msg):
    rospy.loginfo("Status: %s",msg.status.text)
    if (msg.status.status != 2 and msg.status.status != 6 and msg.status.status != 7 and msg.status.status != 8):
        return_to_base()

def callback_movebase_goal(msg):
    goal = msg.goal.target_pose.pose
    goal.position.x = round(goal.position.x)
    goal.position.y = round(goal.position.y)
    goal.orientation.z = round(goal.orientation.z)
    goal.orientation.w = round(goal.orientation.w)

    global send_home
    if goal == home:
        send_home = False
    else:
        send_home = True
    rospy.loginfo("Destination is Home? %r", not send_home)


def return_to_base():
    global send_home
    if send_home == True:
        rospy.loginfo("Returning to home base in 5 seconds...")
        time.sleep(5)

        baseGoal = MoveBaseGoal()
        baseGoal.target_pose.header.frame_id = "map"
        baseGoal.target_pose.header.stamp = rospy.Time.now()
        baseGoal.target_pose.pose.position =  home.position
        baseGoal.target_pose.pose.orientation =  home.orientation

        action = actionlib.SimpleActionClient(robotName+"/move_base", MoveBaseAction)
        action.send_goal(baseGoal)
    return


## **Global Variables**
home = Pose()
send_home = True
robotName = ""

## **Main**
if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            robotName = sys.argv[1]

        home.position = Point(0.0, 0.0, 0.0)
        home.orientation = Quaternion(0.0, 0.0, 1.0, 1.0)

        rospy.init_node(robotName+'_move_base_py')
        rospy.Subscriber('/'+robotName+'/move_base/goal', MoveBaseActionGoal, callback_movebase_goal)
        rospy.Subscriber('/'+robotName+'/move_base/result', MoveBaseActionResult, callback_movebase_result)
        
        if len(sys.argv) > 1:
            rospy.loginfo("Listenning on %s...", robotName)
        else:
            rospy.loginfo("Listenning...")

        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("Except Thrown!")

