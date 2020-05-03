import PIL.Image
import PIL.ExifTags
from decimal import Decimal
import os

dir_name = r'D:\_deep_learning_data_5\_from_tel/'
f = open(dir_name + "out.txt","w+")

for file_name in os.listdir(dir_name):

    if file_name[-3:] == 'jpg':

        src = dir_name + file_name
        print(src)

        img = PIL.Image.open(src)
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }

        GPSInfo = exif['GPSInfo']
        ExifImageWidth = exif['ExifImageWidth']
        ExifImageHeight = exif['ExifImageHeight']
        Resolution = exif['XResolution']
        FocalLength = exif['FocalLength'][0] / exif['FocalLength'][1]
        DateTimeOriginal = exif['DateTimeOriginal']
        Make = exif['Make']
        Model = exif['Model']
        Orientation = exif['Orientation']
        FocalLengthIn35mmFilm = exif['FocalLengthIn35mmFilm']
        ScaleKoef = FocalLengthIn35mmFilm / FocalLength
        Scale1 = 36 / ScaleKoef
        Scale2 = ExifImageHeight / Scale1

        gpsinfo = {}
        for key in exif['GPSInfo'].keys():
            decode = PIL.ExifTags.GPSTAGS.get(key, key)
            gpsinfo[decode] = exif['GPSInfo'][key]
        # print(gpsinfo)

        if len(GPSInfo) != 0:
            for i in GPSInfo:
                # print (i, GPSInfo[i])
                if i == 2:
                    x1 = GPSInfo[i][0][0]
                    x2 = GPSInfo[i][1][0]
                    x3 = GPSInfo[i][2][0] / GPSInfo[i][2][1]
                if i == 4:
                    y1 = GPSInfo[i][0][0]
                    y2 = GPSInfo[i][1][0]
                    y3 = GPSInfo[i][2][0] / GPSInfo[i][2][1]
                if i == 17:
                    a1 = GPSInfo[i][0] / GPSInfo[i][1]

            x = str(x1) + '.' + str(x2)
            y = str(y1) + '.' + str(y2)

            xx = Decimal(x1) + Decimal(x2) / 60 + Decimal(x3) / 3600
            yy = Decimal(y1) + Decimal(y2) / 60 + Decimal(y3) / 3600

            xx = round(xx, 10)
            yy = round(yy, 10)

        print("{},{} angle {}".format(yy, xx, a1))
        f.write("{} xy = {},{} angle = {} \n".format(file_name, yy, xx, a1))
