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
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "../mask_rcnn_road_signs_0030_all.h5")
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

dirname = 'D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/'

for filename in os.listdir(dirname):
    f_type = filename[-3:]
    f_file = filename[:-8]
    if f_type == 'txt':
        f = io.open(dirname + filename, mode="r", encoding="utf-8")
        # ff = io.open(dirname + f_file + '_out_out.csv', mode="w+", encoding="utf-8")
        # f = io.open("D:/TEMP/_deeplearning/road_signs/__video/VID_20200114_102753_out.txt", mode="r",
        #             encoding="utf-8")
        # ff = io.open("D:/TEMP/_deeplearning/road_signs/__video/VID_20200114_102753_out_out.txt", mode="w+",
        #              encoding="utf-8")

        i = 1
        for x in f:
            x = x.split(";")
            file_image = (x[5]).strip()
            # file_image = dirname + '_out_' + f_file + '/' + file_image + '.jpg'

            image = skimage.io.imread(dirname + '_out_' + f_file + '/' + file_image + '.jpg')
            # image = skimage.io.imread("D:/TEMP/_deeplearning/road_signs/__video/out2/" + file_image + '.jpg')

            results = model.detect([image], verbose=1)

            # Visualize results
            r = results[0]

            # visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])

            if len(r['class_ids']) >= 1:
                # print(file_image, len(r['class_ids']))
                color_img = display_instances(image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
                output_file_name = os.path.join(dirname + 'out_image/', f_file + '_' + file_image + '.jpg')
                skimage.io.imsave(output_file_name, color_img)

                # l = str(i) + '; ' + file_image + '; 1' + '\n'
                # l = str(i) + ';' + (x[1]).strip() + ';' + (x[2]).strip() + ';' + (x[3]).strip() + \
                #     ';' + (x[4]).strip() + ';' + (x[5]).strip() + ';1' + '\n'
                l = str(i) + ';' + (x[1]).strip() + ';' + (x[2]).strip() + ';' + (x[3]).strip() + \
                    ';' + "D:/TEMP/_deeplearning/road_signs/_video_25_01_2020/out_image/" + f_file + '_' + file_image + '.jpg' + \
                    ';' + f_file + '_' + file_image + '.jpg' + \
                    ';1' + '\n'
                ff = io.open(dirname + 'all_out.csv', mode="a", encoding="utf-8")
                ff.write(l)
                ff.close()
            # else:
                # l = str(i) + '; ' + file_image + '; 0' + '\n'
                # l = str(i) + ';' + (x[1]).strip() + ';' + (x[2]).strip() + ';' + (x[3]).strip() + \
                #     ';' + (x[4]).strip() + ';' + (x[5]).strip() + ';0' + '\n'
                # ff.write(l)
            i = i + 1
        f.close()
