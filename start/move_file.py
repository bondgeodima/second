import json
import os
import shutil

with open('D:/TEMP/_deeplearning/road_signs/__all/3.34/via_region_data_val.json') as json_file:
    annotations = json.load(json_file)
    annotations = list(annotations.values())  # don't need the dict keys

    # The VIA tool saves images in the JSON even if they don't have any
    # annotations. Skip unannotated images.
    annotations = [a for a in annotations if a['regions']]

    # Add images
    for a in annotations:
        # Get the x, y coordinaets of points of the polygons that make up
        # the outline of each object instance. There are stores in the
        # shape_attributes (see json format above)
        file_name = a['filename']

        print (file_name)
        # os.rename('D:/TEMP/_deeplearning/road_signs/__all/3.34/' + file_name,
        #             'D:/TEMP/_deeplearning/road_signs/__all/3.34/val/' + file_name)
        shutil.move('D:/TEMP/_deeplearning/road_signs/__all/3.34/' + file_name,
                    'D:/TEMP/_deeplearning/road_signs/__all/3.34/val/' + file_name)
