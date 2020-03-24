#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy
import cv2
import json
import argparse
import time
from enum import Enum

import proto

# TODO:
# Finds a list of targets in an image.
# Input:
#   image: an image object defined in proto
#   verbose: a boolean, true to provide verbose output.
# Output:
#   returns a list of target objects corresponding to all targets found in the image

def find_targets(image, verbose):
    # Check if index.json exists. If not, create one
    # check all targets in index.json


    image.dead_reckon(100,100)  # Test

    return

# checks against a list of targets to determine if a target is redundant
#
#
def target_is_redundant(target, targetlist):
    return

# TODO:
# Checks a candidate target to determine of the image is a false positive or redundant
#
# returns:
#   None:   this is a valid image
#   target obj: this is redundant with another target
def target_validation(image,target,targetlist):
    return

# TODO:
# Returns potential matches between the image and a reference image
#
#
#
#
#
def sift_match(img, ref):
    return


# Perform preprocessing on an image
# high frequency noise filtering
# edge sharpening
#
def pre_process(img):
    return


# TODO:
# If run as main, display results to screen and console.
# If run as module, pass back the image and target objects
# If run as module with verbose, do both

if __name__ == '__main__':
    print('target_search as main')
    # Build functionality to test this directly
    # if run from console, pass in a file path
    # this script displays the original image and all found objects to windows, and prints img and target objects to console
    parser = argparse.ArgumentParser()


    find_targets()
else:
    print('target search called by {}'.format(__name__))
    print('behavior unsupported.')
