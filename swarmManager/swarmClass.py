import xml.etree.cElementTree as ET
import ArrayLists




def CreateProductBot(productBot):
    print("You have chosen", productBot, "product bots")
    for i in range(productBot):
        ArrayLists.arrayOfProd.append("Product_Bot"+ str(i))
    print("This is the list of product bots:", ArrayLists.arrayOfProd, '\n')
    for i in range(productBot):
        tree = ET.parse("GazeboBotLaunch.xml")
        root = tree.getroot()

        oldName = root.find("./arg[@name='x']")
        newName = ArrayLists.arrayOfProd[i]
        oldName.attrib["name"] = newName

        oldName1 = root.find("./arg[@default='y']")
        newName1 = ArrayLists.arrayOfProd[i]
        oldName1.attrib["default"] = newName1

        groupArgOld = root.find("./group[@ns ='z']")
        groupArgNew = '$(arg ' + ArrayLists.arrayOfProd[i] + ')'
        groupArgOld.attrib["ns"] = groupArgNew

        paramValOld = root.find("./group/node/param[@value = 'z']")
        paramValNew = '$(arg ' + ArrayLists.arrayOfProd[i] + ')'
        paramValOld.attrib["value"] = paramValNew

        nodeArgsOld = root.find("./group/node[@args = 'u']")
        nodeArgsNew = '-urdf -model $(arg ' + ArrayLists.arrayOfProd[i] + ') -x $(arg x_pos) -y $(arg y_pos) -z $(arg z_pos) -Y $(arg yaw) -param robot_description'
        nodeArgsOld.attrib["args"] = nodeArgsNew

        paramCommandOld = root.find("./group/param[@command ='j']")
        paramCommandNew = '$(find xacro)/xacro --inorder $(find turtlebot3_description)/urdf/turtlebot3_burger.urdf.xacro'
        paramCommandOld.attrib["command"] = paramCommandNew

        oldPosX = root.find("./arg[@default='p']")
        newPosX = str(i)+'.0'
        oldPosX.attrib["default"] = newPosX

        oldPosY = root.find("./arg[@default='q']")
        newPosY = '1.0'
        oldPosY.attrib["default"] = newPosY

        tree.write(str(i)+'Product.launch')
        tree.parse(str(i)+'Product.launch')
        root = tree.getroot()


def CreateProcessBot(processBot):

    print("Now", processBot, "process bots are created")
    for i in range(processBot):
        ArrayLists.arrayOfProc.append("Process_Bot"+ str(i))
    print("This is the list of process bots:", ArrayLists.arrayOfProc, '\n')
    for i in range(processBot):
        tree = ET.parse("GazeboBotLaunch.xml")
        root = tree.getroot()

        oldName = root.find("./arg[@name='x']")
        newName = ArrayLists.arrayOfProc[i]
        oldName.attrib["name"] = newName

        oldName1 = root.find("./arg[@default='y']")
        newName1 = ArrayLists.arrayOfProc[i]
        oldName1.attrib["default"] = newName1

        groupArgOld = root.find("./group[@ns ='z']")
        groupArgNew = '$(arg ' + ArrayLists.arrayOfProc[i] + ')'
        groupArgOld.attrib["ns"] = groupArgNew

        paramValOld = root.find("./group/node/param[@value = 'z']")
        paramValNew = '$(arg ' + ArrayLists.arrayOfProc[i] + ')'
        paramValOld.attrib["value"] = paramValNew

        nodeArgsOld = root.find("./group/node[@args = 'u']")
        nodeArgsNew = '-urdf -model $(arg ' + ArrayLists.arrayOfProc[i] + ') -x $(arg x_pos) -y $(arg y_pos) -z $(arg z_pos) -Y $(arg yaw) -param robot_description'
        nodeArgsOld.attrib["args"] = nodeArgsNew

        paramCommandOld = root.find("./group/param[@command ='j']")
        paramCommandNew = '$(find xacro)/xacro --inorder $(find turtlebot3_description)/urdf/turtlebot3_waffle.urdf.xacro'
        paramCommandOld.attrib["command"] = paramCommandNew

        oldPosX = root.find("./arg[@default='p']")
        newPosX = '0.5'
        oldPosX.attrib["default"] = newPosX

        oldPosY = root.find("./arg[@default='q']")
        newPosY = str(i)+'.0'
        oldPosY.attrib["default"] = newPosY

        tree.write(str(i)+'Process.launch')
        tree.parse(str(i)+'Process.launch')
        root = tree.getroot()


def MakeBotLaunch():
    root = ET.Element("launch")
    group = ET.SubElement(root,"group")
    for i in range(len(ArrayLists.arrayOfProd)):
        ET.SubElement(group, 'include', file='$(find PACKAGE)/PATH/'+str(i)+'Product.launch')
    group1 = ET.SubElement(root,"group")
    for i in range(len(ArrayLists.arrayOfProc)):
        ET.SubElement(group1, 'include', file='$(find PACKAGE)/PATH/'+str(i)+'Process.launch')
    includeFile = ET.fromstring('''
    <include file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="world_name" value="$(find gazebo_worlds)/worlds/factory_floor.sdf"/>
        <arg name="paused" value="false"/>
        <arg name="use_sim_time" value="true"/>
        <arg name="gui" value="true"/>
        <arg name="headless" value="false"/>
        <arg name="debug" value="false"/>
</include> ''')
    root.append(includeFile)

    tree = ET.ElementTree(root)
    tree.write("BotLaunch.launch")

