import io
import psycopg2

dir_in = 'D:/TEMP/agro/file/'

conn = psycopg2.connect(dbname='dzk', user='postgres',
                        password='gagra321', host='192.168.33.57')
cursor = conn.cursor()
cursor.execute('SELECT cadnum, ST_AsGeoJSON(the_geom_tr,3) FROM mirbank.ss')
for row in cursor:
    fff = io.open(dir_in + row[0].replace(":","") + '.json', mode="w", encoding="utf-8")
    fff.write(row[1])
    print(row[1])
    fff.close()