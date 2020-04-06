import json

filename_in = 'E:/signs/val/via_region_data.json'
with open(filename_in, "r") as read_file:
    data = json.load(read_file)
c = 0
k = 0
for i in data:
    if data[i]['regions']:
        for n in data[i]['regions']:
            # data[i]['regions'][n]['region_attributes']={'class': '1'}
            # print(i, data[i]['regions'][n]['region_attributes'])
            c = c + 1
    else:
        k = k + 1
print('Number of records: ', c, 'Number of bad: ', k)