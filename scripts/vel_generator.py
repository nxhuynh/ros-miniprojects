#!/usr/bin/env python
## Simple velocity generator for intoxicated turtle
## publishes geometry_msgs/Twist messages
## to the 'turtle1/cmd_vel' topic

import rospy
from geometry_msgs.msg import Twist, Vector3

def velocity_generator():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('vel_generator', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        linear = Vector3(2.0, 0.0, 0.0)
        angular = Vector3(0.0, 0.0, 1.8)
        ve = Twist(linear, angular)
        rospy.loginfo(str(ve))
        pub.publish(ve)
        rate.sleep()

if __name__ == '__main__':
    try:
        velocity_generator()
    except rospy.ROSInterruptException:
        pass
