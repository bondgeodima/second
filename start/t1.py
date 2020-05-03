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

"""
s = '0ab10c2CaB12'.strip()
def rle_decode(s):
    repeat = ""
    res = ""
    for e in s:
        if e.isdigit():
            repeat += e
        else:
            if repeat:
                res += e * int(repeat)
            else:
                res += e
            repeat = ""
    return res

print(rle_decode(s))
"""

"""
s = '15.5 mile in yard'.strip().split()
d = {"mile": 1609, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254, "km": 1000, "m": 1, "cm": 0.01, "mm": 0.001}
x = float(s[0]) * (d[s[1]] / d[s[3]])
print("{:.2e}".format(x))
"""

"""
In = str (input('Enter your name: '))
print ('Hello ' + (In))
"""

"""
s = 100
i = 1
ss = ""
while s > 0:
    ss = ss + i*str(i)
    i += 1
    s -= 1
print(" ".join(list(str(ss[:i-1]))))
"""

"""
s = int(input())
ss = ''
for i in range(1, s+1):
    if len(ss) < s:
        ss += i*str(i)
print(' '.join(list(str(ss[:i]))))
"""

"""
def get_int(start_message, error_message, end_message):
    while True:
        if start_message:
            print(start_message)
            start_message = None
        try:
            s = int(input())
            print(end_message)
            return s
            break
        except:
            print(error_message)


x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
"""

"""
x = (-12+6/17)/(((1+2)**4)-5*8)
print(x)
"""

"""
while True:
    try:
        x = int(input())
        if x == -10 or (x > -5 and x <= 3) or (x>8 and x<12) or x>=16:
            print('True')
        else:
            print('False')
    except:
        print("not str")
"""

s = input()
ss = s.title().replace('_','')
# for i in range(0, len(ss)):
#     ss[i] = ss[i].capitalize()
# ss = "".join(ss)
print(ss)