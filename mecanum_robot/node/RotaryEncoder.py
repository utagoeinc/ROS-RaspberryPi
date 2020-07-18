#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from mecanum_robot.msg import motor
import time
from customClass.RotaryEncoder import RotaryEncoder

rf_pins = [16, 12]
rb_pins = [21, 20]
lf_pins = [24, 23]
lb_pins = [4, 18]


def rotaryEncoder():
    rospy.init_node('rotary_encoder', anonymous=True)
    pub = rospy.Publisher('motor_info', motor, queue_size=10)
    msg = motor()

    re_rf = RotaryEncoder(rf_pins)
    re_rb = RotaryEncoder(rb_pins)
    re_lf = RotaryEncoder(lf_pins)
    re_lb = RotaryEncoder(lb_pins)

    r = rospy.Rate(1000)
    while not rospy.is_shutdown():
        re_rf.countRotary()
        re_rb.countRotary()
        re_lf.countRotary()
        re_lb.countRotary()
        is_changed = re_rf.is_changed or re_rb.is_changed or re_lf.is_changed or re_lb.is_changed
        if is_changed:
            msg.rf_count = re_rf.counter
            msg.rb_count = re_rb.counter
            msg.lf_count = re_lf.counter
            msg.lb_count = re_lb.counter
            pub.publish(msg)
        r.sleep()

if __name__ == "__main__":
    try:
        rotaryEncoder()
    except rospy.ROSInterruptException:
        pass

