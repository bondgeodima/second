# Для создания нового файла анотаций надо через программу FastStone произвести трансформацию
# изображения(уменьшить размер). Трансформацию необходимо провести в отдельную папку. В эту же
# папку необходимо скопировать файл исходный файл via_region_data.json. Потредактировать тело программы
# в зависимости от того какой процент искажения и в какой папке находяться данные "_p_25".
# Результаты будут записываться в файл via_region_data_out.json
# Не доконца разобрался какой алгоритм изменения координат. Все зависит от того как программ VIA
# поворачивает изображение, когда открывает его!!!

import os
import sys
import json
# import numpy as np
from PIL import Image

i = 0

data = {}
dataset_dir = os.path.abspath("D:\\TEMP\\_deeplearning\\__from_kiev\\____sign\\2.3\\_val\\p_90_b_150")
sys.path.append(dataset_dir)

annotations = json.load(open(os.path.join(dataset_dir, "via_region_data.json")))
annotation = list(annotations.values())  # don't need the dict keys
# print (annotations["2_2018-08-21 10-13-22.jpg1482534"])

# The VIA tool saves images in the JSON even if they don't have any
# annotations. Skip unannotated images.
# annotation = [a for a in annotation if a['filename']]

for key, value in annotations.items():
    # Get the x, y coordinaets of points of the polygons that mggt[1]
    filename = value['filename']
    filename = filename.split('.',1)[0] + '_b_150.jpg'
    newsize = os.stat(os.path.join(dataset_dir, filename)).st_size
    newfilename = filename+str(newsize)
    value['size'] = os.stat(os.path.join(dataset_dir, filename)).st_size
    value['filename'] = filename
    key = newfilename

    img = Image.open(os.path.join(dataset_dir, filename))
    width, height = img.size

    # all_points_y = [width - round(r * 0.5) for r in value['regions']['0']['shape_attributes']['all_points_y']]
    # value['regions']['0']['shape_attributes']['all_points_x'] = all_points_y
    # value['regions']['0']['shape_attributes']['all_points_y'] = all_points_x
    # print (filename, width, height)
    # data[key] = value

#    for r in value['regions']:
        # all_points_x = r['shape_attributes']['all_points_x']
        # ll_points_y = r['shape_attributes']['all_points_y']

        # для исходных изображений класса 2_1 (т.е. самых первых изображений) такой алгоритм

#        all_points_x = [round(s * 0.90) for s in r['shape_attributes']['all_points_x']]
#        all_points_y = [width - round(s * 0.90) for s in r['shape_attributes']['all_points_y']]

        # для изображений которые прошли обработку через растровый редактор такой алгоритм
#        all_points_x = [round(s * 0.1) for s in r['shape_attributes']['all_points_x']]
#        all_points_y = [round(s * 0.1) for s in r['shape_attributes']['all_points_y']]

#        if 640 < width < 1280:
#            all_points_x = [round(s * 0.25) for s in r['shape_attributes']['all_points_x']]
#            all_points_y = [width - round(s * 0.25) for s in r['shape_attributes']['all_points_y']]
#        else:
#            all_points_x = [round(s * 0.25) for s in r['shape_attributes']['all_points_y']]
#            all_points_y = [round(s * 0.25) for s in r['shape_attributes']['all_points_x']]

#        all_points_x = [width - s for s in r['shape_attributes']['all_points_x']]
#        all_points_y = [s for s in r['shape_attributes']['all_points_y']]

        # print (str(all_points_x) + ' ' + str(all_points_y))
        # для исходных изображений класса 2_1 (т.е. самых первых изображений) такой алгоритм
#        r['shape_attributes']['all_points_x'] = all_points_y
#        r['shape_attributes']['all_points_y'] = all_points_x

        # для изображений которые прошли обработку через растровый редактор такой алгоритм
#        r['shape_attributes']['all_points_x'] = all_points_x
#        r['shape_attributes']['all_points_y'] = all_points_y

        # print (filename, width, height)
    data[key] = value

with open(os.path.join(dataset_dir, "via_region_data_out.json"), "w") as jsonFile:
    json.dump(data, jsonFile)