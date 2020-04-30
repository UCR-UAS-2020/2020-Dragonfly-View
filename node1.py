#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def talker():
    pub = rospy.Publisher('node1_to_relay', Image, queue_size=10)
    rospy.init_node('node1', anonymous=True)
    rate = rospy.Rate(1)
    cv_image = cv2.imread('meme.jpg')
    msg = CvBridge().cv2_to_imgmsg(cv_image, "bgr8")
    while not rospy.is_shutdown():
        msg.header.stamp = rospy.get_rostime()
        #rospy.loginfo(msg)
        pub.publish(msg)
        print('sent')
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass