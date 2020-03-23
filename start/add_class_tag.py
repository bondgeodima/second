import json

filename_in = 'E:/signs/train/train.json'
with open(filename_in, "r") as read_file:
    data = json.load(read_file)
c = 0
for i in data:
    if data[i]['regions']:
        for n in data[i]['regions']:
            data[i]['regions'][n]['region_attributes']={'class': '1'}
            print(i, data[i]['regions'][n]['region_attributes'])
    c = +1
out_file = open('E:/signs/train/out.json','w')
out_file.write(json.dumps(data))
out_file.close()
print('Number of records: ', c)