#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from jetbot_ros.msg import cmd_raw

pub = rospy.Publisher('jetbot_ros/cmd_raw', cmd_raw, queue_size=1)

def callback(msg):
#	rospy.loginfo("Recieved a /cmd_vel message!")
#	rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
#	rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))
	axis1 = msg.linear.x
	axis2 = msg.angular.z
        lmot = 0.0
        rmot = 0.0

        if axis1 > 0 and axis2 == 0: # Forward   
		rmot = axis1
                lmot = axis1
        elif axis1 > 0 and axis2 > 0: # Forward Left Turn 
		rmot = axis1  
 		lmot = axis1 - axis2
  	elif axis1 > 0 and axis2 < 0: # Forward Right Turn
		rmot = axis1 - abs(axis2)
		lmot = axis1
	elif axis1 < 0 and axis2 == 0: # Reverse
		rmot = axis1
		lmot = axis1
	elif axis1 < 0 and axis2 > 0: # Reverse Left Turn 
		rmot = axis1 - axis2
		lmot = axis1
	elif axis1 < 0 and axis2 < 0: # Reverse Right Turn
		rmot = axis1
		lmot = axis1 - abs(axis2)
	elif axis1 == 0 and axis2 < 0: # Rotate Left
		rmot = 0.0
                lmot = abs(axis2)
	elif axis1 == 0 and axis2 > 0: # Rotate Right
	        rmot = axis2
	        lmot = 0.0
        elif axis1 == 0 and axis2 == 0: # Stop
		rmot = 0.0
		lmot = 0.0

        msg = cmd_raw()
#	rospy.loginfo("Right Motor = :[%f]"%(rmot))
#	rospy.loginfo("Left Motor = :[%f]"%(lmot))
	msg.left = lmot
	msg.right = rmot
	pub.publish(msg)
#       rospy.loginfo("msg.left =:[%f]"%(msg.left))
#       rospy.loginfo("msg.right =:[%f]"%(msg.right))

def start():
    global pub
    rospy.init_node('teleop_read')
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
	start()
