from ordered_set import OrderedSet
import ast

dir_name = r'D:\_english/'
f = open(dir_name + "coldest_place.txt", "r+")
f_dict = open(dir_name + "dict_all.csv","r+")
dict = []
lines = f.read().split('\n')
lines_dict = f_dict.read().split('\n')
t = lines_dict
for x in t:
    # print(x.split(';')[0])
    dict.append(x.split(';')[0])

s = set(" ".join(lines).replace('.', ' ').replace(',', ' ').replace('"', '').lower().split(" "))

thisset = s

i = 0
for x in thisset:
    if x not in dict:
        print(x)
        i += 1
