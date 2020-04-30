#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String

class Relay:
    def __init__(self):
        self.sender1 = rospy.Publisher("relay_to_node2", Image, queue_size=10)
        self.sender2 = rospy.Publisher("relay_to_node3", Image, queue_size=10)
        self.listener1 = rospy.Subscriber("node1_to_relay", Image, self.callback1)
        self.listener2 = rospy.Subscriber("node2_to_relay", Image, self.callback2)

    def callback1(self, data):
        rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.header)
        self.sender1.publish(data)
        print('done')

    def callback2(self, data):
        rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.header)
        self.sender2.publish(data)
        print('done')

if __name__ == '__main__':
    Relay()
    rospy.init_node('relay', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")