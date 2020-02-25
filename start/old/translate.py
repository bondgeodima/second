import psycopg2
from googletrans import Translator
translator = Translator()

conn = psycopg2.connect(dbname='gis', user='postgres',
                        password='postgres', host='192.168.33.88')
cursor = conn.cursor()
#cursor.execute('SELECT p.osm_id, p.name, p,tags FROM tmp.planet_osm_point p WHERE osm_id = 1127675851')

#cursor.execute("select p.osm_id, p.name from planet_osm_point p, tmp.krim_polygon kp where st_intersects(kp.geom, p.way) = 't' and p.name is not null and tags -> 'name:uk' is not null limit 1")
#cursor.execute("select p.osm_id, p.name from planet_osm_point p, tmp.krim_polygon kp where st_intersects(kp.geom, p.way) = 't' and p.name is not null and p.place in ('village','town','city') and tags -> 'name:uk' is null")

#result_set = cursor.fetchall()
#for row in result_set:
#    print (row[2])
#    n = row[1]
#    translation = translator.translate(n, src='ru', dest='uk')
#    print(translation.origin, ' -> ', translation.text)

cursor.execute("UPDATE tmp.planet_osm_point SET tags = tags || 'name:uk => Вавілон'::hstore WHERE osm_id = 1127675851")

conn.commit()
cursor.close()
conn.close()