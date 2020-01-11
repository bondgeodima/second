import io
f = io.open("D:/TEMP/_deeplearning/road_signs/__video/VID_20200111_102822.srt", mode="r", encoding="utf-8")
a = []
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
while i < (len(a)-4):
    print(a[i], a[i+3][:8], a[i+3][11:19], a[i+3][22:27], a[i+3][30:33])
    i = i + 4
