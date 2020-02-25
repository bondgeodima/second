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
# from PIL import Image
import PIL.Image
import PIL.ExifTags
from PIL import ImageEnhance

file_json_in = 'via_region_data.json'

list_scale = [1.0, 0.25, 0.50, 0.75]
list_bright = [1.0, 0.5, 1.5]

ending = ''
head = {}

for l_s in list_scale:
    scale = str(l_s).split('.', 1)[1].ljust(2,'0')
    ending_1 = ending + '_p_' + str(scale)
    for l_b in list_bright:

        koef = l_s
        file_json_out = 'via_region_data_out'
        bright = (str(l_b).split('.', 1)[0] + str(l_b).split('.', 1)[1]).ljust(3, '0')
        ending_2 = ending_1 + '_b_' + str(bright)
        file_name = ''
        file_json_out = file_json_out + ending_2 + '.json'

        data = {}
        data_set_dir = os.path.abspath("D:\\TEMP\\_deeplearning\\__from_kiev\\____sign\\all\\val")
        data_out_dir = os.path.abspath("D:\\TEMP\\_deeplearning\\__from_kiev\\____sign\\all_out\\val")
        sys.path.append(data_set_dir)

        annotations = json.load(open(os.path.join(data_set_dir, file_json_in)))
        annotation = list(annotations.values())  # don't need the dict keys

        for key, value in annotations.items():
            file_name = value['filename']

            file_patch = data_set_dir + '\\' + file_name
            img = PIL.Image.open(file_patch)
            width, height = img.size

            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in PIL.ExifTags.TAGS
            }

            size = width * koef, height * koef
            Orientation = exif['Orientation']

            for r in value['regions']:
                if Orientation == 6:
                    all_points_x = [round(s * koef) for s in r['shape_attributes']['all_points_x']]
                    # Для исходного изображения
                    all_points_y = [round(s * koef) for s in r['shape_attributes']['all_points_y']]
                    r['shape_attributes']['all_points_x'] = all_points_x
                    r['shape_attributes']['all_points_y'] = all_points_y
                    # Для  изображения которое прошло через трансформацию и было записано на диск
                    # all_points_y = [width - round(s * 0.5) for s in r['shape_attributes']['all_points_y']]
                    # r['shape_attributes']['all_points_x'] = all_points_y
                    # r['shape_attributes']['all_points_y'] = all_points_x
                if Orientation == 1:
                    all_points_x = [round(s * koef) for s in r['shape_attributes']['all_points_x']]
                    all_points_y = [round(s * koef) for s in r['shape_attributes']['all_points_y']]
                    r['shape_attributes']['all_points_x'] = all_points_x
                    r['shape_attributes']['all_points_y'] = all_points_y

            new_file_name = str(file_name).split('.', 1)[0] + ending_2 + '.jpg'
            out_file = data_out_dir + '\\' + new_file_name
            img.thumbnail(size, PIL.Image.ANTIALIAS)

            img = ImageEnhance.Contrast(img)
            img = img.enhance(l_b)  # set FACTOR > 1 to enhance contrast, < 1 to decrease

            img.save(out_file, "JPEG")

            file_size = os.stat(os.path.join(data_out_dir, new_file_name)).st_size
            value['size'] = file_size
            value['filename'] = new_file_name
            new_file_name = new_file_name + str(file_size)
            key = new_file_name

            data[key] = value

        # print (data)

        head.update(data)

        # with open(os.path.join(data_out_dir, file_json_out), "w") as jsonFile:
        #     json.dump(data, jsonFile)

with open(os.path.join(data_out_dir, "out.json"), "w") as jsonFile:
    json.dump(head, jsonFile)



