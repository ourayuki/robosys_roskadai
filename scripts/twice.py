#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import String

def cb(message):
    m  = random.choice("abc")
    if m =='a':
        n = ' credit'
    else:
        n = ' garbage'

    rospy.loginfo(message.data+n)

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', String, cb)
    rospy.spin()
