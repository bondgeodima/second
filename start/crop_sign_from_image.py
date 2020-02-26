import os
import json
import cv2
import numpy as np
import PIL.Image
import PIL.ExifTags

l = []

# dir_name = 'D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/3.34/'
dir_name = 'D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/part_1/train/'
# file_json = '3_34.json'
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
        print (file_name)

        # Get the x, y coordinaets of points of the polygons that make up
        # the outline of each object instance. There are stores in the
        # shape_attributes (see json format above)
        # polygons = [r['shape_attributes'] for r in a['regions'].values()]
        # objects = [s['region_attributes'] for s in a['regions'].values()]
        # class_ids = [int(n['class']) for n in objects]
        all_points_x = [r['shape_attributes']['all_points_x'] for r in a['regions'].values()]
        all_points_y = [r['shape_attributes']['all_points_y'] for r in a['regions'].values()]
        # print (all_points_x, all_points_y)
        img = cv2.imread(dir_name + file_name)

        imge = PIL.Image.open(dir_name + file_name)

        img_exif = imge._getexif()

        if img_exif:
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in imge._getexif().items()
                if k in PIL.ExifTags.TAGS
            }

            Orientation = exif['Orientation']

        polygons = []
        for i in range(len(all_points_x)):
            polygon =[]
            # points = []
            for j in range(len(all_points_x[i])):
                pt = []
                pt.append(int(all_points_y[i][j]))
                pt.append(int(all_points_x[i][j]))
                polygon.append(pt)
                # points.append(pt)

            pts = np.array(polygon)
            rect = cv2.boundingRect(pts)
            y, x, w, h = rect
            croped = img[y:y+w, x:x+h].copy()

            pts = pts - pts.min(axis=0)

            mask = np.zeros(croped.shape[:2], np.uint8)
            cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

            ## (3) do bit-op
            dst = cv2.bitwise_and(croped, croped, mask=mask)

            ## (4) add the white background
            bg = np.ones_like(croped, np.uint8) * 255
            cv2.bitwise_not(bg, bg, mask=mask)
            dst2 = bg + dst

            dim = (64, 64)
            croped = cv2.resize(croped, dim, interpolation=cv2.INTER_AREA)

            cv2.imwrite('D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/out/_' + file_name[:-4] + '_'
                        + str(i) + '_croped.png', croped)
            # cv2.imwrite('D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/out/' + 'mask.png', mask)
            # cv2.imwrite('D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/out/' + 'dst.png', dst)
            # cv2.imwrite('D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/out/' + 'dst2.png', dst2)

            polygons.append(polygon)
        print (polygons)


