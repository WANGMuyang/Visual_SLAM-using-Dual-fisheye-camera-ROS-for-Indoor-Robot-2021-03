#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class image_publisher():
    def __init__(self):
        self.cv_bridge = CvBridge()
        self.pub = rospy.Publisher('camera/image_raw', Image, queue_size=1)
    
    def image_cb(self):
        img = cv2.imread("/home/alpha/openvslam_backup/image_localization/image_localization6.png",1)
        img_msg = self.cv_bridge.cv2_to_imgmsg(img,encoding="bgr8")
        self.pub.publish(img_msg)


if __name__ == '__main__':
    rospy.init_node("single_image_publisher", anonymous=True)
    single = image_publisher()
    a=1
    while(a<200):
        a+=1
        single.image_cb()
