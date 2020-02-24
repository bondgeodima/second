import cv2
import os
import io
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

from skimage import measure
from pycocotools import mask
from skimage.filters import threshold_otsu
from scipy.spatial import ConvexHull
import json

# Root directory of the project
ROOT_DIR = os.path.abspath("C:/Users/Administrator/Mask_RCNN")

print(ROOT_DIR)

sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize

sys.path.append(os.path.join(ROOT_DIR, ""))  # To find local version
from samples.coco import coco

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# detect signs by type
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "../mask_rcnn_road_signs_0030_all_data_all_layers.h5")
# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    # single sign detect
    NUM_CLASSES = 1 + 1  # 1 Background + 1 Building


config = InferenceConfig()
config.display()

# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(COCO_MODEL_PATH, by_name=True)

class_names = ['BG', 'road_sign']

def random_colors(N):
    np.random.seed(1)
    colors = [tuple(255 * np.random.rand(3)) for _ in range(N)]
    return colors

def apply_mask(image, mask, color, alpha=0.5):
    """apply mask to image"""
    for n, c in enumerate(color):
        image[:, :, n] = np.where(
            mask == 1,
            image[:, :, n] * (1 - alpha) + alpha * c,
            image[:, :, n]
        )
    return image

def display_instances(image, boxes, masks, ids, names, scores):
    """
        take the image and results and apply the mask, box, and Label
    """
    n_instances = boxes.shape[0]
    colors = random_colors(n_instances)

    if not n_instances:
        print('NO INSTANCES TO DISPLAY')
    else:
        assert boxes.shape[0] == masks.shape[-1] == ids.shape[0]

    for i, color in enumerate(colors):
        if not np.any(boxes[i]):
            continue

        y1, x1, y2, x2 = boxes[i]
        label = names[ids[i]]
        score = scores[i] if scores is not None else None
        caption = '{} {:.2f}'.format(label, score) if score else label
        mask = masks[:, :, i]

        image = apply_mask(image, mask, color)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        image = cv2.putText(
            image, caption, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2
        )

    return image

dirname = 'D:/TEMP/_deeplearning/road_signs/_video_17_02_2020/_out_VID_20200130_102654/'

for filename in os.listdir(dirname):

    f_type = filename[-3:]
    f_file = filename[:-8]

    image = skimage.io.imread(dirname + filename)

    results = model.detect([image], verbose=1)

    # Visualize results
    r = results[0]

    output_image = display_instances(image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])

    output_file_name = os.path.join(dirname + 'out_image/', filename)
    skimage.io.imsave(output_file_name, output_image)