#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from mecanum_robot.msg import mecanum
from mecanum_robot.msg import motor
from module.MecanumWheels import *


def setMsgStop(msg):
    motor_speed = stop()
    msg.target_rf = motor_speed[0]
    msg.target_rb = motor_speed[1]
    msg.target_lf = motor_speed[2]
    msg.target_lb = motor_speed[3]

# def setMsgModeName(msg, mode_name_op, speed):
#     motor_speed = mode_name_op(speed)
#     msg.rf = motor_speed[0]
#     msg.rb = motor_speed[1]
#     msg.lf = motor_speed[2]
#     msg.lb = motor_speed[3]

def setMsgNormal(msg, direction, speed):
    motor_speed = normalMove(direction, speed)
    msg.target_rf = motor_speed[0]
    msg.target_rb = motor_speed[1]
    msg.target_lf = motor_speed[2]
    msg.target_lb = motor_speed[3]

def setMsgParallel(msg, direction, speed):
    motor_speed = parallelMove(direction, speed)
    msg.target_rf = motor_speed[0]
    msg.target_rb = motor_speed[1]
    msg.target_lf = motor_speed[2]
    msg.target_lb = motor_speed[3]

def mecanum_callback(sub_msg):

    pub = rospy.Publisher('motor_info', motor, queue_size=10)
    pub_msg = motor()

    mode_name = sub_msg.mode
    direction = sub_msg.direction
    speed = sub_msg.speed

    if sub_msg.stop:
        setMsgStop(pub_msg)
        pub.publish(pub_msg)

    if mode_name == 'normal':
        setMsgNormal(pub_msg, direction, speed)
        pub.publish(pub_msg)
    elif mode_name == 'parallel':
        setMsgParallel(pub_msg, direction, speed)
        pub.publish(pub_msg)
    # else:
    #     setMsgModeName(pub_msg, mode_name, speed)
    #     pub.publish(pub_msg)


def MecanumControl():
    rospy.init_node('MecanumController', anonymous=True)
    rospy.Subscriber('mecanum_robot', mecanum, mecanum_callback, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    MecanumControl()