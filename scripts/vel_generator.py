#!/usr/bin/env python
## Simple velocity generator for intoxicated turtle
## publishes geometry_msgs/Twist messages
## to the 'turtle1/cmd_vel' topic

import rospy
from geometry_msgs.msg import Twist, Vector3
import random

def velocity_generator():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('vel_generator', anonymous=True)
    rate = rospy.Rate(10) # 1hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        if random.random() < 0.5:
            sign = -1.0
        else:
            sign = 1.0
        linear = Vector3(random.random() * 3, 0.0, 0.0)
        angular = Vector3(0.0, 0.0, random.random() * 2 * 3.14 * sign)
        ve = Twist(linear, angular)
        rospy.loginfo(str(ve))
        pub.publish(ve)
        rate.sleep()

if __name__ == '__main__':
    try:
        velocity_generator()
    except rospy.ROSInterruptException:
        pass
