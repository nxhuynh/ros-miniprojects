#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')

import rospy
import tf
import math

if __name__ == '__main__':
    rospy.init_node('dynamic_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    mood = 2.5
    sign = 1.0
    prev_t = rospy.Time.now().to_sec()
    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec()
        if t - prev_t > 2:
            prev_t = t
            if mood > 3:
                sign = -1.0
            elif mood < 1:
                sign = 1.0
            mood = mood + sign*1
        #br.sendTransform((2.0 * math.sin(t), 2.0 * math.cos(t), 0.0),
        br.sendTransform((0.0, mood, 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "carrot1",
                         "turtle1")
        rate.sleep()

