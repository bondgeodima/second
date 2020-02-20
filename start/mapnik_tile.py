import math
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  #print (xtile,ytile)
  #return (xtile, ytile)
  return xyz_to_meta("ajt", xtile, ytile, zoom)


def xyz_to_meta(xmlname, x,y, z):
    METATILE = 8
    mask = METATILE -1
    x &= ~mask
    y &= ~mask
    hashes = {}

    for i in range(0,5):
        hashes[i] = ((x & 0x0f) << 4) | (y & 0x0f)
        x >>= 4
        y >>= 4

    meta = "%s/%s/%d/%u/%u/%u/%u/%u.meta" % ("/var/lib/mod_tile", xmlname, z, hashes[4], hashes[3], hashes[2], hashes[1], hashes[0])
    return meta


if __name__ == '__main__':
    print (deg2num(50.547179, 30.457586, 16))
    # print (xyz_to_meta("default", 38297, 22118, 16))