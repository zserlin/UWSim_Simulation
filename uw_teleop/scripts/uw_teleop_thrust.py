#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Joy, Image
from nav_msgs.msg import Odometry


import os.path as op


class UWTeleop(object):
    def __init__(self):
        rospy.init_node("keyboard")


        self.force_pub = rospy.Publisher('/NEXXUS_ROV/thrusters_input', Float64MultiArray, queue_size=10)
        self.rate = rospy.Rate(20)



        self.joy_sub = rospy.Subscriber("/joy", Joy, self.joy_msg_callback)

        self.joy_data = Joy()
        self.vel_cmd = Float64MultiArray()



    def joy_msg_callback(self, data):
        '''
        joy_data.axes = [+left, +forward, +yaw, +up, +pitch, +roll]

        joy_data.buttons = [take_pictures, ...]
        '''

        self.joy_data = data
        x = np.rint(self.joy_data.axes[1]) * 100
        y = np.rint(self.joy_data.axes[3]) * 100
        z = np.rint(self.joy_data.axes[0]) * 100
        self.vel_cmd.data = [x,x,y,y,z]

    def start_teleop(self):
        while not rospy.is_shutdown():
            self.force_pub.publish(self.vel_cmd)
            self.rate.sleep()

if __name__ == "__main__":
    uw_teleop = UWTeleop()
    uw_teleop.start_teleop()
