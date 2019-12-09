#!/usr/bin/env python

from __future__ import print_function
import os
import roslib
import sys
import rospy
import cv2
from os import environ
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from nav_msgs.msg import Odometry
from smart_battery_msgs.msg import SmartBatteryStatus
from kobuki_msgs.msg import SensorState
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# Reads the TB1 Configuration XML File
tb3ConfigFile = et.parse('tb3Settings.xml')
# Find the root element from the file (in this case "environment")
root = tb3ConfigFile.getroot()
# Save the Robot Selected
tb3_namespace = root.findtext('TB3_ROS_NAMESPACE')
print(tb3_namespace)

kobuki_base_max_charge = 160

def callback(data):
    try:
        self.bridge = CvBridge()
        rgb_image = self.bridge.imgmsg_to_cv2(data, "rgb8")
    except CvBridgeError as e:
        print(e)

def callbackOdom(msg):
    odomValues= str(msg.pose.pose)

def notebookBattery(data):
    notebookBatteryValue = str(data.percentage)

def kobukiBattery(self,data):    
    kobukiBatteryValue = rospy.loginfo(str(round(float(data.battery) / float(self.kobuki_base_max_charge) * 100)))

def main():
    rospy.init_node('roc', anonymous=True)
    image_sub = rospy.Subscriber(tb3_namespace+"/tb1_image",Image,callback)
    odom_sub = rospy.Subscriber(tb3_namespace+'/odom',Odometry,callbackOdom)
    noteBatt_sub = rospy.Subscriber(tb3_namespace+"/laptop_charge/",
                                    SmartBatteryStatus,
                                    notebookBattery)
    kobukiBatt_sub = rospy.Subscriber(tb3_namespace+"/mobile_base/sensors/core",
                                      SensorState,
                                      kobukiBattery)
    rospy.spin()

if __name__ == "__main__":
    main()