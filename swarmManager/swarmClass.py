import xml.etree.cElementTree as ET

arrayOfProd = []
arrayOfProc = []


class Swarm:
    def __init__(self, productBot, processBot):
        self.productBot = productBot
        self.processBot = processBot


def CreateProductBot(productBot):
    print("You have chosen", productBot, "product bots")
    for i in range(productBot):
        arrayOfProd.append("Product Bot"+ str(i))
    print("This is the list of product bots:", arrayOfProd, '\n')
    for i in range(productBot):
        tree = ET.parse('GazeboBotLaunch.xml')
        root = tree.getroot()

        oldName = root.find("./arg[@name='x']")
        newName = arrayOfProd[i]
        oldName.attrib["name"] = newName

        oldName1 = root.find("./arg[@default='y']")
        newName1 = arrayOfProd[i]
        oldName1.attrib["default"] = newName1

        groupArgOld = root.find("./group[@ns ='z']")
        groupArgNew = '$(arg ' + arrayOfProd[i] + ')'
        groupArgOld.attrib["ns"] = groupArgNew

        paramValOld = root.find("./group/node/param[@value = 'z']")
        paramValNew = '$(arg ' + arrayOfProd[i] + ')'
        paramValOld.attrib["value"] = paramValNew

        nodeArgsOld = root.find("./group/node[@args = 'u']")
        nodeArgsNew = '-urdf -model $(arg ' + arrayOfProd[i] + ') -x $(arg x_pos) -y $(arg y_pos) -z $(arg z_pos) -Y $(arg yaw) -param robot_description'
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
        arrayOfProc.append("Process Bot"+ str(i))
    print("This is the list of process bots:", arrayOfProc, '\n')
    for i in range(processBot):
        tree = ET.parse('GazeboBotLaunch.xml')
        root = tree.getroot()

        oldName = root.find("./arg[@name='x']")
        newName = arrayOfProc[i]
        oldName.attrib["name"] = newName

        oldName1 = root.find("./arg[@default='y']")
        newName1 = arrayOfProc[i]
        oldName1.attrib["default"] = newName1

        groupArgOld = root.find("./group[@ns ='z']")
        groupArgNew = '$(arg ' + arrayOfProc[i] + ')'
        groupArgOld.attrib["ns"] = groupArgNew

        paramValOld = root.find("./group/node/param[@value = 'z']")
        paramValNew = '$(arg ' + arrayOfProc[i] + ')'
        paramValOld.attrib["value"] = paramValNew

        nodeArgsOld = root.find("./group/node[@args = 'u']")
        nodeArgsNew = '-urdf -model $(arg ' + arrayOfProc[i] + ') -x $(arg x_pos) -y $(arg y_pos) -z $(arg z_pos) -Y $(arg yaw) -param robot_description'
        nodeArgsOld.attrib["args"] = nodeArgsNew

        paramCommandOld = root.find("./group/param[@command ='j']")
        paramCommandNew = '$(find xacro)/xacro --inorder $(find turtlebot3_description)/urdf/turtlebot3_waffle.urdf.xacro'
        paramCommandOld.attrib["command"] = paramCommandNew

        oldPosX = root.find("./arg[@default='p']")
        newPosX = '1.0'
        oldPosX.attrib["default"] = newPosX

        oldPosY = root.find("./arg[@default='q']")
        newPosY = str(i)+'.0'
        oldPosY.attrib["default"] = newPosY

        tree.write(str(i)+'Process.launch')
        tree.parse(str(i)+'Process.launch')
        root = tree.getroot()


def MakeBotLaunch():
    root = ET.Element("Launch")
    group = ET.SubElement(root,"Group")
    for i in range(len(arrayOfProd)):
        ET.SubElement(group, 'include', file='$(find PACKAGE)/PATH/'+str(i)+'Product.launch')
    group1 = ET.SubElement(root,"Group")
    for i in range(len(arrayOfProc)):
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

