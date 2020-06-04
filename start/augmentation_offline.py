import os
import json
import cv2
import numpy as np
import PIL.Image
import PIL.ExifTags

import imgaug.augmenters as iaa

l = []

# dir_name = 'D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/3.34/'
# dir_name = r'D:\TEMP\_deeplearning\__from_kiev\____sign\all\train/'
# dir_name = 'D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/part_1/train/'
# file_json = '3_34.json'
dir_name = r'E:\signs\train/'
file_json = 'via_region_data.json'

augmentation = iaa.Sequential([
    # iaa.Affine(scale=(0.5, 1)),
    iaa.Scale(0.5)
    # iaa.Affine(translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}),
    # iaa.Affine(rotate=(-10, 10)),
    # iaa.GaussianBlur(sigma=(0.0, 2.0)),
    # iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0))
])

with open(dir_name + file_json) as json_file:
    annotations = json.load(json_file)
    annotations = list(annotations.values())  # don't need the dict keys

    # The VIA tool saves images in the JSON even if they don't have any
    # annotations. Skip unannotated images.
    annotations = [a for a in annotations if a['regions']]


    # Add images
    for a in annotations:
        file_name = a['filename']

        # print(len(regions))
        img = cv2.imread(dir_name + file_name)
        img = cv2.resize(img, (600, 800))
        cv2.imshow("img", img)
        img_aug = augmentation.augment_image(img)
        cv2.imshow("img_aug", img_aug)
        # cv2.imwrite('E:/signs/img_aug/v_' + file_name[:-4] + '_c_' + str(k)
        #             + '.png', img_aug)

