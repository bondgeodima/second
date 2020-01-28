import cv2
import os

dirname = 'D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/'


for filename in os.listdir(dirname):
    f_type = filename[-3:]
    f_file = filename[:-4]
    if f_type == 'mp4':
        out_name = 'D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/_out_' + f_file + '/'
        vidcap = cv2.VideoCapture(dirname + filename)
        # vidcap = cv2.VideoCapture('D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/VID_20200125_154626.mp4')
        success,image = vidcap.read()
        count = 0
        print("start " + filename)
        while success:
            # cv2.imwrite("D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/_out_VID_20200125_154626/%05d.jpg" % count, image)     # save frame as JPEG file
            cv2.imwrite(out_name + "%05d.jpg" % count, image)  # save frame as JPEG file
            success,image = vidcap.read()
            # print('Read a new frame: ', success)
            count += 1
        print("finish " + filename)