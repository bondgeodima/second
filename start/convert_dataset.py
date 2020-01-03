import os
from shutil import copyfile

dir_in = 'C:/Users/Administrator/nanonets_object_tracking-master/crops/'
dir_out = 'C:/Users/Administrator/cosine_metric_learning-master/Nano-dataset/bounding_box_train/'

for folder in os.listdir(dir_in):
    dir_folder = 'C:/Users/Administrator/nanonets_object_tracking-master/crops/' + folder
    for file in os.listdir(dir_folder):
        filename = file
        filename = filename.split("_")
        seq = filename[0][-1:]
        camera = filename[1][-1:]
        frame = filename[2]
        object_id = filename[3].split(".")[0]
        file_type = filename[3].split(".")[1]
        new_filename = object_id.zfill(4) + "_c" + camera + "s" + seq + "_" + frame.zfill(6) + "_01.jpg"
        src = dir_in + folder + "/" + file
        dst = dir_out + new_filename
        print(src, dst)
        copyfile(src, dst)

