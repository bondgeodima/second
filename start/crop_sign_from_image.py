import os
import json
import cv2

l = []

with open('D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/3_34.json') as json_file:
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
        img = cv2.imread(file_name)

        polygons = []
        for i in range(len(all_points_x)):
            polygon =[]
            pts = []
            for j in range(len(all_points_x[i])):
                pt = []
                pt.append(all_points_x[i][j])
                pt.append(all_points_y[i][j])
                polygon.append(pt)
                pts.append(pt)

            rect = cv2.boundingRect(pts)
            x, y, w, h = rect
            croped = img[y:y + h, x:x + w].copy()

            pts = pts - pts.min(axis=0)

            mask = np.zeros(croped.shape[:2], np.uint8)
            cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

            ## (3) do bit-op
            dst = cv2.bitwise_and(croped, croped, mask=mask)

            ## (4) add the white background
            bg = np.ones_like(croped, np.uint8) * 255
            cv2.bitwise_not(bg, bg, mask=mask)
            dst2 = bg + dst

            cv2.imwrite("croped.png", croped)
            cv2.imwrite("mask.png", mask)
            cv2.imwrite("dst.png", dst)
            cv2.imwrite("dst2.png", dst2)

            polygons.append(polygon)
        print (polygons)


