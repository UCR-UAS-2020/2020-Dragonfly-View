#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Objects for use elsewhere.

from enum import Enum

class Color(Enum):
    White = 1
    Black = 2
    Gray = 3
    Red = 4
    Blue = 5
    Green = 6
    Yellow = 7
    Purple = 8
    Brown = 9
    Orange = 10

class Shape(Enum):
    Circle = 1
    Semicircle = 2
    Quarter_Circle = 3
    Triangle = 4
    Square = 5
    Rectangle = 6
    Trapezoid = 7
    Pentagon = 8
    Hexagon = 9
    Heptagon = 10
    Octagon = 11
    Star = 12
    Cross = 13

"""
Note: There are hundreds of these by the end of the mission, so try to keep iterables in the Target object instead.

cam_image: Object to hold references of images captured by the camera.

filename: Location of the image (dev: do not store array in memory, these are really big)
targets: targets associated with this image
timestamp: time photo was taken (for sorting)

"""
class CamImage:
    def __init__(self,number,file_path,timestamp,latitude,longitude,altitude,angle):
        self.number = number                    # number in sequence of images
        self.file_path = file_path              # location of jpg in directory
        self.targets = []                       # list of associated targets
        self.timestamp = timestamp              # time image was taken (using module time.time())
        self.latitude = latitude                # position of camera when image was taken
        self.longitude = longitude              # position of camera when image was taken
        self.altitude = altitude                # position of camera when image was taken
        self.angle = angle                      # Tuple representing roll, pitch, yaw when image was taken


    def dead_recon(self, xy_pos):
        # check xy is in range of photo
        # calculations based on angle
        return

"""
There are less than 30 of these total.

"""
class Target:
    def __init__(self, image):
        self.images = []                # list of image objects that this target shares in
        self.crop = None                # a cropped version of this target from the first time it was spotted
        self.type = None                # as required in mission spec
        self.latitude = None            # as required in mission spec
        self.longitude = None           # as required in mission spec
        self.orientation = None         # as required in mission spec
        self.shape = None               # as required in mission spec
        self.background_color = None    # as required in mission spec
        self.alphanumeric = None        # as required in mission spec
        self.alphanumeric_color = None  # as required in mission spec
        self.description = None         # as required in mission spec

    # Link a target and its corresponding image
    def link_target_img(self, img):
        # add image object to self.images
        # add target to img.targets
        return

    # TODO: Create a function that generates a JSON object that matches the specification given here: https://github.com/auvsi-suas/interop#upload-objects
    def to_json(self):
        # use obj.__dict__ as explained here: https://www.tutorialspoint.com/What-does-built-in-class-attribute-dict-do-in-Python
        return

    # TODO: Push file path to index.json (check if it exists tho)
    def push_index(self):
        return

# Independent functions:


# Generate index.json
# If overwrite is true, this will create a blank index even if there is a index.json file present.
# If overwrite is false, this will only create an index if there is none there
# returns True if overwritten, False otherwise
# index.json should contain only a blank imagelist object and a blank targetlist object
def make_index(directory_path,overwrite):
    return
