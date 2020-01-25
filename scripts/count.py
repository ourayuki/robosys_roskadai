#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import String
rospy.init_node('count')
pub = rospy.Publisher('count_up', String, queue_size=1)
rate = rospy.Rate(1)
global n
while not rospy.is_shutdown():
    m  = random.choice("abc")
    if m =='a':
        n = 'You get robosys'
    elif m =='b': 
        n = 'You get unk'
    elif m == 'c':
        n = 'you get all'
    pub.publish(n)
    rate.sleep()
