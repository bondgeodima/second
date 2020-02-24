import io
import os

dirname = 'D:/TEMP/_deeplearning/road_signs/_video_17_02_2020/'

for filename in os.listdir(dirname):
    f_type = filename[-3:]
    f_file = filename[:-4]
    if f_type == 'srt':
        f = io.open(dirname + filename, mode="r", encoding="utf-8")
        ff = io.open(dirname + f_file + '_out.txt', mode="w+", encoding="utf-8")
        # ff = io.open("D:/TEMP/_deeplearning/road_signs/__video/VID_20200114_102753_out.txt", mode="w+",
        #              encoding="utf-8")
        a = []
        b = []
        for x in f:
            if len(x) > 1 and len(x) < 100:
                # print(x)
                x = x.strip('\n')
                a.append(x)

        f.close()
        print (a)
        print(len(a))
        step = 2
        i = 0
        с = 0
        while i < (len(a)-4):
            # print(a[i], a[i+3][:8], a[i+3][10:18], a[i+3][20:27], a[i+3][30:33])
            b = a[i+3].split(",")
            x = str(b[0]) + '.' + str(b[1])
            y = str(b[2]) + '.' + str(b[3])
            angle = b[4]
            # p = 'D:\\TEMP\\_deeplearning\\road_signs\\__video\\out2\\'
            p = 'D:\\TEMP\\_deeplearning\\road_signs\\_video_17_02_2020\\_out_' + f_file + '\\'
            file = str(с).zfill(5)
            l = str(a[i]) + '; ' + x + ';' + y + ';' + angle + '; ' + p + file + '.jpg' + '; ' + file + '\n'
            print (a[i], x, y, angle, p + file + '.jpg', file)
            ff.write(l)
            i = i + 4
            с = с + 24

        ff.close()
