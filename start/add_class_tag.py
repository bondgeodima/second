import json
import io

with open('E:/signs/val/val.json') as json_file:
    annotations = json.load(json_file)

    for i in annotations:
        # temp = a['regions']['region_attributes']
        #temp.append(class_list)
        for n in annotations[i]['regions']:
            annotations[i]['regions'][n]['region_attributes']['class'] = '1'
            print (annotations[i])

    fff = io.open('E:/signs/train/' + 'via_region_data.json', mode="w", encoding="utf-8")
    json.dump(annotations, fff)