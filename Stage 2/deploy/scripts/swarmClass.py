import xml.etree.cElementTree as ET
import ArrayLists


def CreateProductBot(productBot):
    print("You have chosen", productBot, "product bots")
    for i in range(productBot):
        ArrayLists.arrayOfProd.append("Product_Bot" + str(i))
        ArrayLists.arrayOfInv.append(0)
    print("This is the list of product bots:", ArrayLists.arrayOfProd, '\n')
    for i in range(productBot):
        tree = ET.parse("GazeboBotLaunch.xml")
        root = tree.getroot()

        oldName = root.find("./include/arg[@value='Bot1']")
        newName = ArrayLists.arrayOfProd[i]
        oldName.attrib["value"] = newName

        oldPosX = root.find("./include/arg[@value='x']")
        newPosX = str(i)+'.0'
        oldPosX.attrib["value"] = newPosX

        oldPosY = root.find("./include/arg[@value='y']")
        newPosY = '1.0'
        oldPosY.attrib["value"] = newPosY

        oldModel = root.find("./include/arg[@value='robot']")
        newModel = 'burger'
        oldModel.attrib["value"] = newModel

        tree.write(str(i)+'Product.launch')
        tree.parse(str(i)+'Product.launch')
        root = tree.getroot()


def CreateProcessBot(processBot):

    print("Now", processBot, "process bots are created")
    for i in range(processBot):
        ArrayLists.arrayOfProc.append("Process_Bot" + str(i))
    print("This is the list of process bots:", ArrayLists.arrayOfProc, '\n')
    for i in range(processBot):
        tree = ET.parse("GazeboBotLaunch.xml")
        root = tree.getroot()

        oldName = root.find("./include/arg[@value='Bot1']")
        newName = ArrayLists.arrayOfProd[i]
        oldName.attrib["value"] = newName

        oldPosX = root.find("./include/arg[@value='x']")
        newPosX = '5.0'
        oldPosX.attrib["value"] = newPosX

        oldPosY = root.find("./include/arg[@value='y']")
        newPosY = str(i)+'.0'
        oldPosY.attrib["value"] = newPosY

        oldModel = root.find("./include/arg[@value='robot']")
        newModel = 'waffle'
        oldModel.attrib["value"] = newModel

        tree.write(str(i)+'Process.launch')
        tree.parse(str(i)+'Process.launch')
        root = tree.getroot()


def MakeBotLaunch():
    root = ET.Element("launch")
    group = ET.SubElement(root, "group")
    for i in range(len(ArrayLists.arrayOfProd)):
        ET.SubElement(group, 'include', file='$(find PACKAGE)/PATH/'+str(i)+'Product.launch')
    group1 = ET.SubElement(root, "group")
    for i in range(len(ArrayLists.arrayOfProc)):
        ET.SubElement(group1, 'include', file='$(find PACKAGE)/PATH/'+str(i)+'Process.launch')
    includeFile1 = ET.fromstring('''
    <!-- Visualization and map/world location -->
    <group>
        <arg name="map_file"    default="$(find deploy)/maps/factory_map.yaml"/>
        <arg name="world_file"  default="$(find deploy)/worlds/factory_floor.sdf"/>
        <arg name="open_rviz"   default="true"/>
        <arg name="open_gazebo" default="true"/>
    </group>
    ''')
    includeFile2 = ET.fromstring('''
    <!-- Map server -->
    <node pkg="map_server" name="map_server" type="map_server" args="$(arg map_file)">
        <param name="frame_id" value="map"/>
    </node> \n
    ''')
    includeFile3 = ET.fromstring('''
    <!-- Rviz -->
    <group if="$(arg open_rviz)"> 
        <node pkg="rviz" type="rviz" name="rviz" output="screen" args="-d $(find deploy)/rviz/basic_config.rviz"/>
    </group> \n
    ''')
    includeFile4 = ET.fromstring('''
    <!-- Gazebo -->
    <group if="$(arg open_gazebo)"> 
        <include file="$(find gazebo_ros)/launch/empty_world.launch">
            <arg name="world_name" value="$(arg world_file)"/>
        </include> 
    </group>\n''')

    root.append(includeFile1)
    root.append(includeFile2)
    root.append(includeFile3)
    root.append(includeFile4)

    tree = ET.ElementTree(root)
    tree.write("BotLaunch.launch")

