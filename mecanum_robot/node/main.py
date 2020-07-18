#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from mecanum_robot.msg import mecanum
import time

def stopMove():
    pub = rospy.Publisher('mecanum_robot', mecanum, queue_size=10)
    msg = mecanum()
    msg.stop = True
    pub.publish(msg)

def parallCircle(msg, pub):
    r = rospy.Rate(10)
    msg.mode = 'parallel'
    msg.speed = 0.5
    msg.stop = False
    direction = 1
    while True:
        direction = direction - 0.03
        if direction <= -1:
            msg.direction = 0
            msg.speed = 0
            msg.stop = True
            pub.publish(msg)
            break
        msg.direction = direction
        pub.publish(msg)
        r.sleep()

def rotateR(msg, pub):
    r = rospy.Rate(10)
    msg.mode = 'normal'
    msg.speed = 0.5
    msg.direction = -0.5
    msg.stop = False

    start_time = time.time()
    d_time = 3.2
    while True:
        elapsed_time = time.time() - start_time
        pub.publish(msg)
        if elapsed_time > d_time:
            stopMove()
            break
        r.sleep()

# def move8(msg, pub):
#     msg.mode = 'paralell'
#     msg.stop = False
#     msg.speed = 0.7

#     while True:

def pub_for_sec(t, pub, msg):
    start_time = time.time()
    d_time = 0
    while d_time < t:
        pub.publish(msg)
        d_time = time.time() - start_time


def main():
    rospy.init_node('main', anonymous=True, disable_signals=True)
    pub = rospy.Publisher('mecanum_robot', mecanum, queue_size=10)

    msg = mecanum()

    # parallCircle(msg, pub)
    # time.sleep(1)
    # rotateR(msg, pub)
    

    msg.mode = 'normal'
    msg.direction = 0
    msg.speed = 0.5
    msg.stop = False
    # pub_for_sec(4, pub, msg)
    # stopMove()
    # time.sleep(1)
    # msg.direction = 1
    # pub_for_sec(4, pub, msg)
    # stopMove()


    # msg.mode = 'parallel'
    # msg.speed = 0.5
    # msg.direction = -0.5
    # msg.stop = False
    # pub_for_sec(3.5, pub, msg)
    # stopMove()
    # time.sleep(1)
    # msg.direction = 0.5
    # pub_for_sec(3.5, pub, msg)
    # stopMove()


    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(msg)
        r.sleep()




if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        stopMove()
