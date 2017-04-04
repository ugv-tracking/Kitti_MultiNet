#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Copyright (c) 2015 PAL Robotics SL.
Released under the BSD License.
Created on 7/14/15
@author: Sammy Pfeiffer
test_video_resource.py contains
a testing code to see if opencv can open a video stream
useful to debug if video_stream does not work
"""
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
'''

import json
import logging
import os
import cv2
import sys

sys.path.insert(1, os.path.realpath('../incl/MultiNet/incl'))
sys.path.insert(1, os.path.realpath('../incl/MultiNet'))



if __name__ == '__main__':

    #resource = sys.argv[1]
    resource = '/home/xulingyun/tusimple.mp4'
    cap = cv2.VideoCapture(resource)
    if not cap.isOpened():
        print "Error opening resource: " + str(resource)
        print "Maybe opencv VideoCapture can't open it"
        exit(0)

    print "Correctly opened resource, starting to show feed."
    rval, frame = cap.read()
    while rval:
        cv2.imshow("Stream", frame)
        rval, frame = cap.read()
        key = cv2.waitKey(20)
        # print "key pressed: " + str(key)
        # exit on ESC, you may want to uncomment the print to know which key is ESC for you
        if key == 27 or key == 1048603:
            break
            cv2.destroyWindow("preview")

