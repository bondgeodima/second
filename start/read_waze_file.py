import json
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from collections import Counter

l = []
with open('D:/TEMP/_____НИГДе/waze_19_12/2019_12_19_00_00_WAZE_JSON.json') as json_file:
    annotations = json.load(json_file)
    annotations = list(annotations.values())  # don't need the dict keys

    # The VIA tool saves images in the JSON even if they don't have any
    # annotations. Skip unannotated images.
    annotations = [a for a in annotations if a['alerts']]

    # Add images
    for a in annotations:
        # Get the x, y coordinaets of points of the polygons that make up
        # the outline of each object instance. There are stores in the
        # shape_attributes (see json format above)
        type_a = [r['type'] for r in a['alerts'].values()]
        location = [s['location'] for s in a['alerts'].values()]
        # class_ids = [int(n['class']) for n in objects]
        # l = l + class_ids

        print (type_a)
    # print (Counter(l))

    # size, scale = 1000, 10
    # commutes = pd.DataFrame({'col':l})
    # commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
    #                    color='#607c8e')
    # plt.title('Commute Times for 1,000 Commuters')
    # plt.xlabel('Counts')
    # plt.ylabel('Commute Time')
    # plt.grid(axis='y', alpha=0.75)