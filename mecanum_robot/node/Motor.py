#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from mecanum_robot.msg import motor
from gpiozero import Motor

rf_pins = [17, 27]
rb_pins = [19, 13]
lf_pins = [6, 5]
lb_pins = [25, 22]

rf = Motor(rf_pins[0], rf_pins[1])
rb = Motor(rb_pins[0], rb_pins[1])
lf = Motor(lf_pins[0], lf_pins[1])
lb = Motor(lb_pins[0], lb_pins[1])

def motorMove(motor, speed):
    if speed >= 0:
        motor.forward(speed)
    else:
        motor.backward(-speed)

def motor_callback(msg):
    target_rf = msg.target_rf
    target_rb = msg.target_rb
    target_lf = msg.target_lf
    target_lb = msg.target_lb


    output_rf = target_rf
    output_rb = target_rb
    output_lf = target_lf
    output_lb = target_lb

    motorMove(rf, output_rf)
    motorMove(rb, output_rb)
    motorMove(lf, output_lf)
    motorMove(lb, output_lb)


def main():
    rospy.init_node('Motor', anonymous=True)
    rospy.Subscriber('motor_info', motor, motor_callback, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    main()