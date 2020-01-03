import json
import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from collections import Counter

dirname = 'D:/TEMP/_____НИГДе/waze_19_12/'
f = open("D:/TEMP/_____НИГДе/waze_19_12/project/3.txt", "w+")

for filename in os.listdir(dirname):
    f_type = filename[-4:]
    if f_type == 'json':
        date = filename[:10]
        time = filename[11:16]
        # print('filename: {}, date: {}, time {}'.format(filename, date, time))

        with open('D:/TEMP/_____НИГДе/waze_19_12/'+filename) as json_file:
            annotations = json.load(json_file)
            annotations = annotations['alerts']

            # Add images
            for a in annotations:
                # Get the x, y coordinaets of points of the polygons that make up
                # the outline of each object instance. There are stores in the
                # shape_attributes (see json format above)
                # country = a['country']
                # nThumbsUp = a['nThumbsUp']
                # magvar = a['magvar']
                # reportRating = a['reportRating']
                # confidence = a['confidence']
                # reliability = a['reliability']
                type_a = a['type']
                subtype = a['subtype']
                location = a['location']
                uuid = a['uuid']
                # class_ids = [int(n['class']) for n in objects]
                # l = l + class_ids

                # print ('country: {} nThumbsUp: {} magvar: {} reportRating: {} confidence: {} '
                #        'reliability: {} type: {} subtype {} location {}'.format(country, nThumbsUp, magvar, reportRating,
                #                                                                 confidence, reliability, type_a, subtype,
                #                                                                 location))

                # print ('type: {} subtype {} X {} Y {}'.format(type_a, subtype, location['x'], location['y']))

                # print('{}; {}; {}; {}; {}; {}'.format(type_a, subtype, location['x'], location['y'], date, time))
                f.write('{}; {}; {}; {}; {}; {}; {} \r\n'.format(uuid, type_a, subtype, location['x'], location['y'], date, time))
f.close()
    # print (Counter(l))

    # size, scale = 1000, 10
    # commutes = pd.DataFrame({'col':l})
    # commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
    #                    color='#607c8e')
    # plt.title('Commute Times for 1,000 Commuters')
    # plt.xlabel('Counts')
    # plt.ylabel('Commute Time')
    # plt.grid(axis='y', alpha=0.75)