import math


ab = int(input())
bc = int(input())
m=math.sqrt(ab**2+bc**2)
s=round(math.degrees(math.acos(bc/m)))
print(str(s)+chr(176))
