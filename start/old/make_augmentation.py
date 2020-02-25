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

koef = 0.25
while koef < 1:
    i = 0
    j = 0
    koef_str = str(koef).split('.', 1)[1].ljust(2,'0')
    koef_str = '_p_' + koef_str + '.jpg'
    file_json_in = 'via_region_data.json'
    file_json_out = 'via_region_data_out_' + str(koef).split('.', 1)[1].ljust(2,'0') + '.json'

    data = {}
    data_set_dir = os.path.abspath("D:\\TEMP\\_deeplearning\\__from_kiev\\____sign\\all\\train")
    data_out_dir = os.path.abspath("D:\\TEMP\\_deeplearning\\__from_kiev\\____sign\\all_out\\train")
    sys.path.append(data_set_dir)

    annotations = json.load(open(os.path.join(data_set_dir, file_json_in)))
    annotation = list(annotations.values())  # don't need the dict keys

    # The VIA tool saves images in the JSON even if they don't have any
    # annotations. Skip unannotated images.
    # annotation = [a for a in annotation if a['filename']]

    for key, value in annotations.items():
        # Get the x, y coordinaets of points of the polygons that mggt[1]
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
                i += 1
            if Orientation == 1:
                all_points_x = [round(s * koef) for s in r['shape_attributes']['all_points_x']]
                all_points_y = [round(s * koef) for s in r['shape_attributes']['all_points_y']]
                r['shape_attributes']['all_points_x'] = all_points_x
                r['shape_attributes']['all_points_y'] = all_points_y
                j += 1

        file_name = file_name.split('.', 1)[0] + koef_str
        out_file = data_out_dir + '\\' + file_name
        img.thumbnail(size, PIL.Image.ANTIALIAS)
        img.save(out_file, "JPEG")

        # contrast_50 = ImageEnhance.Contrast(img)
        # contrast_50 = contrast_50.enhance(0.5)  # set FACTOR > 1 to enhance contrast, < 1 to decrease
        # contrast_50.save(data_out_dir + '\\' + 'b_50_' + file_name)

        # contrast_150 = ImageEnhance.Contrast(img)
        # contrast_150 = contrast_150.enhance(1.5)  # set FACTOR > 1 to enhance contrast, < 1 to decrease
        # contrast_150.save(data_out_dir + '\\' + 'b_150_' + file_name)

        file_size = os.stat(os.path.join(data_out_dir, file_name)).st_size
        new_file_name = file_name + str(file_size)
        value['size'] = file_size
        value['filename'] = new_file_name
        key = new_file_name

        data[key] = value

    with open(os.path.join(data_out_dir, file_json_out), "w") as jsonFile:
        json.dump(data, jsonFile)

    koef = koef + 0.25
