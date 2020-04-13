"""
# Шифр цезаря
a = int(3)
b = 'i am caesar'.strip()
alfavit = " abcdefghijklmnopqrstuvwxyz"
shifr = []
for i in b:
    shifr.append(alfavit[(alfavit.index(i)+a)%len(alfavit)])
mySTR = "".join(shifr)
print('Result: "{}"'.format(mySTR))
"""


