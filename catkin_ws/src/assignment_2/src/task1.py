#!/usr/bin/env python

import rospy
import sys
from geometry_msgs.msg import Twist

#making function
def move_turtle(linear_v,angular_v):
    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
 
    vel = Twist()
    while not rospy.is_shutdown():
        
	vel.linear.x = linear_v
	vel.linear.y = 0
	vel.linear.z = 0
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = angular_v


        rospy.loginfo("Linear Vel = %f: Angular Vel = %f",linear_v,angular_v)

        pub.publish(vel)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle(float(5.0),float(2))
    except rospy.ROSInterruptException:
        pass
