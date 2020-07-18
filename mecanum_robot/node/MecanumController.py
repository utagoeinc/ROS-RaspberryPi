#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from mecanum_robot.msg import mecanum
from customClass.MecanumWheels import MecanumWheels

rf_pins = [17, 27]
rb_pins = [19, 13]
lf_pins = [6, 5]
lb_pins = [25, 22]
wheel_pins = [rf_pins, rb_pins, lf_pins, lb_pins]

mc = MecanumWheels(wheel_pins)

def mecanum_callback(msg):

    mode_name = msg.mode
    speed = msg.speed
    direction = msg.direction

    if msg.stop:
        mc.stop()

    if mode_name == 'normal':
        mc.normalMove(direction, speed)
    elif mode_name == 'parallel':
        mc.parallelMove(direction, speed)
    else:
        mc.stop()


def MecanumControl():
    rospy.init_node('MecanumController', anonymous=True)
    rospy.Subscriber('mecanum_robot', mecanum, mecanum_callback, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    MecanumControl()