import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

l = []
with open('D:/TEMP/_deeplearning/__from_kiev/_new_data_12_12_2019/3_34.json') as json_file:
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
        polygons = [r['shape_attributes'] for r in a['regions'].values()]
        objects = [s['region_attributes'] for s in a['regions'].values()]
        class_ids = [int(n['class']) for n in objects]
        l = l + class_ids

        print (class_ids)
    print (Counter(l))

    size, scale = 1000, 10
    commutes = pd.DataFrame({'col':l})
    commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
                       color='#607c8e')
    plt.title('Commute Times for 1,000 Commuters')
    plt.xlabel('Counts')
    plt.ylabel('Commute Time')
    plt.grid(axis='y', alpha=0.75)