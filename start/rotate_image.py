import cv2
import os

dirname = 'D:/TEMP/_deeplearning/road_signs/_video_17_02_2020/_out_VID_20200130_095321'

for filename in os.listdir(dirname):
    f_type = filename[-3:]
    f_file = filename[:-4]
    if f_type == 'jpg':
        out_name = dirname + filename
        img = cv2.imread(dirname + filename)
        (h, w) = img.shape[:2
                 ]
        # calculate the center of the image
        center = (w / 2, h / 2)

        angle90 = 90
        angle180 = 180
        angle270 = 270

        scale = 1.0

        M = cv2.getRotationMatrix2D(center, angle180, scale)
        rotated180 = cv2.warpAffine(img, M, (w, h))
        cv2.imwrite(out_name, rotated180)
