import os
import json
import cv2
import numpy as np
import PIL.Image
import PIL.ExifTags

l = []

# dir_name = 'D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/3.34/'
# dir_name = r'D:\TEMP\_deeplearning\__from_kiev\____sign\all\train/'
# dir_name = 'D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/part_1/train/'
# file_json = '3_34.json'
dir_name = r'E:\signs\train/'
file_json = 'via_region_data.json'

with open(dir_name + file_json) as json_file:
    annotations = json.load(json_file)
    annotations = list(annotations.values())  # don't need the dict keys

    # The VIA tool saves images in the JSON even if they don't have any
    # annotations. Skip unannotated images.
    annotations = [a for a in annotations if a['regions']]


    # Add images
    for a in annotations:
        file_name = a['filename']
        # print (file_name)

        # Get the x, y coordinaets of points of the polygons that make up
        # the outline of each object instance. There are stores in the
        # shape_attributes (see json format above)
        # polygons = [r['shape_attributes'] for r in a['regions'].values()]
        # objects = [s['region_attributes'] for s in a['regions'].values()]
        # class_ids = [int(n['class']) for n in objects]
        # print(len(regions))
        img = cv2.imread(dir_name + file_name)
        height, width, channels = img.shape

        imge = PIL.Image.open(dir_name + file_name)

        img_exif = imge._getexif()

        Orientation = int()

        if img_exif:
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in imge._getexif().items()
                if k in PIL.ExifTags.TAGS
            }

            Orientation = exif['Orientation']
            print (file_name, Orientation)
        else:
            Orientation = 0
            print(file_name, Orientation)