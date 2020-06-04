import io
import os

dirname = r'E:\signs\ЦОДР\OpenCamera/'

for filename in os.listdir(dirname):
    f_type = filename[-3:]
    f_file = filename[:-4]
    if f_type == 'srt':
        a = []
        f = io.open(dirname + filename, mode="r", encoding="utf-8")
        ff = io.open(dirname + f_file + '_out.txt', mode="w+", encoding="utf-8")
        for x in f:
            if len(x) > 1 and len(x) < 100:
                # print(x)
                x = x.strip('\n')
                a.append(x)
        print (len(a))
        i = 0
        c = 1
        while i < (len(a)-4):
            # print(a[i], a[i+3][:8], a[i+3][10:18], a[i+3][20:27], a[i+3][30:33])
            b = a[i+3].split(",")
            x = str(b[0]) + '.' + str(b[1])
            y = str(b[2]) + '.' + str(b[3])
            angle = b[6]
            # p = 'D:\\TEMP\\_deeplearning\\road_signs\\__video\\out2\\'
            p = 'E:\\signs\\video\\'
            file = str(c).zfill(5)
            l = str(a[i]) + '; ' + x + ';' + y + ';' + angle + '; ' + p + file + '.jpg' + '; ' + file + '\n'
            print (a[i], x, y, angle, p + file + '.jpg', file)
            ff.write(l)
            i = i + 4
            c += 1
        ff.close()