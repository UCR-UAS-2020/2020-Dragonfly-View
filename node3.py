#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def callback(data):
    cv_image = CvBridge().imgmsg_to_cv2(data, "bgr8")
    cv2.imwrite('new_meme.jpg', cv_image)
    
def listener():
    rospy.init_node('node3', anonymous=True)
    rospy.Subscriber("relay_to_node3", Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()