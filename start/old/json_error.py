import os
import sys
import json
from PIL import Image

data = {}
dataset_dir = os.path.abspath("C:\\Users\\Administrator\\Mask_RCNN\\samples\\roadsigns\\road_signs\\train")
sys.path.append(dataset_dir)

annotations = json.load(open(os.path.join(dataset_dir, "via_region_data.json")))
annotations = list(annotations.values())  # don't need the dict keys

# The VIA tool saves images in the JSON even if they don't have any
# annotations. Skip unannotated images.
annotations = [a for a in annotations if a['regions']]

# Add images
for a in annotations:
    # Get the x, y coordinaets of points of the polygons that make up
    # the outline of each object instance. There are stores in the
    # shape_attributes (see json format above)
    polygons = [r['shape_attributes'] for r in a['regions'].values()]
    objects = [s['region_attributes'] for s in a['regions'].values()]
    class_ids = [int(n['class']) for n in objects]
    # load_mask() needs the image size to convert polygons to masks.
    # Unfortunately, VIA doesn't include it in JSON, so we must read
    # the image. This is only managable since the dataset is tiny.
    image_path = os.path.join(dataset_dir, a['filename'])
    print (image_path)

