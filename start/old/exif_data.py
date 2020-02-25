import os
import PIL.Image
import psycopg2
import PIL.ExifTags
import requests
from decimal import Decimal

file_patch = 'D:\\TEMP\\_deeplearning\\__from_kiev\\____sign\\all\\train\\20190621_125753_5_35_2.jpg'

img = PIL.Image.open(file_patch)
exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}

print (exif)

exit()

GPSInfo = exif['GPSInfo']
ExifImageWidth = exif['ExifImageWidth']
ExifImageHeight = exif['ExifImageHeight']
Resolution = exif['XResolution']
FocalLength = exif['FocalLength'][0]/exif['FocalLength'][1]
DateTimeOriginal = exif['DateTimeOriginal']
Make = exif['Make']
Model = exif['Model']
Orientation = exif['Orientation']

FocalLengthIn35mmFilm = exif['FocalLengthIn35mmFilm']
ScaleKoef = FocalLengthIn35mmFilm / FocalLength
Scale1 = 36 / ScaleKoef
Scale2 = ExifImageHeight / Scale1

#s = r['rois'][4] - r['rois'][2]
#s = 76.6
s = 124.21
s2 = s / Scale2
d = round(((FocalLength * 700 / s2)/1000),2)

sign = '5_35_1'

print ('distance = '+str(d))

# print (GPSInfo)
# Need check GPSInfo

if len(GPSInfo) != 0:
    for i in GPSInfo:
        # print (i, GPSInfo[i])
        if i == 2:
            x1 = GPSInfo[i][0][0]
            x2 = GPSInfo[i][1][0]
            x3 = GPSInfo[i][2][0]/GPSInfo[i][2][1]
        if i == 4:
            y1 = GPSInfo[i][0][0]
            y2 = GPSInfo[i][1][0]
            y3 = GPSInfo[i][2][0]/GPSInfo[i][2][1]
        if i == 17:
            a1 = GPSInfo[i][0]/GPSInfo[i][1]

    x = str(x1) + '.' + str(x2)
    y = str(y1) + '.' + str(y2)

    x = Decimal(x)
    y = Decimal(y)

    xx = Decimal(x1) + Decimal(x2)/60 + Decimal(x3)/3600
    yy = Decimal(y1) + Decimal(y2)/60 + Decimal(y3)/3600

    xx = round(xx,10)
    yy = round(yy,10)

    print (xx)
    print (yy)
    print (a1)
    print (FocalLength)

    image_filename = os.path.basename(file_patch)

    print (image_filename)

    multipart_form_data = {
        'file': (image_filename, open(file_patch, 'rb')),
        'mimType': 'image/jpeg',
        'lat': ('', str(xx)),
        'lng': ('', str(yy)),
        'dist': ('', str(d)),
        'angle': ('', str(a1)),
        'focal': ('', str(FocalLength)),
        'sign': ('', str(sign)),
    }
    print (multipart_form_data)
# response = requests.post('http://192.168.33.80:84/php/upload.php/',
#                         files=multipart_form_data)

# print(response.status_code)

#try:
#    connection = psycopg2.connect(user = "postgres",
#                                  password = "postgres",
#                                  host = "192.168.33.89",
#                                  port = "5432",
#                                  database = "geo_new_3")
#    cursor = connection.cursor()
#    cursor.execute('INSERT INTO photo(lat, lng) VALUES (' + str(x) + ',' + str(y) + ')')
#    connection.commit()
#    cursor.execute('SELECT * FROM photo LIMIT 10')
#    for row in cursor:
#        print(row)
#    cursor.close()
#    connection.close()
#except (Exception, psycopg2.DatabaseError) as error :
#    print ("Error while creating PostgreSQL table", error)