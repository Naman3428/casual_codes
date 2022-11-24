#by naman
import math

s1 = int(input("Enter Side 1: "))
s2 = int(input("Enter Side 2: "))
s3 = int(input("Enter Side 3: "))

if s1>s2 and s1>s3:
    h = s1
    b = s2
    l = s3
    if h*h == b*b + l*l:
        area = 1/2*l*b
        print(f"It is a right angled triangle having area {area} units square")

elif s2>s1 and s2>s3:
    h = s2
    b = s1
    l = s3
    if h*h == b*b + l*l:
        area = 1/2*l*b
        print(f"It is a right angled triangle having area {area} units square")


elif s3>s2 and s3>s1:
    h = s3
    b = s2
    l = s1
    if h*h == b*b + l*l:
        area = 1/2*l*b
        print(f"It is a right angled triangle having area {area} units square")


try:
        s = (s1+s2+s3)/2
        area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
        print(f"It is not a right angle triangle but it is having area: {area} square units")

except:
        print("It is not a valid triangle, please enter sides again")
