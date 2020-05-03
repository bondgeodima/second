dir_name = r'D:\_english\netflix/'
f = open(dir_name + "sample.xml.srt", "r+")
ff = open(dir_name + "sample.txt", "w+")
for str in f:
    if str[0:3] == '<i>':
        print (str[3:-5])
        ff.write(str[3:-5] + '\n')
f.close()
ff.close()
