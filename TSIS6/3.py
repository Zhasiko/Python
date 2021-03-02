import math
s=input()
a=[int(s) for s in s.split()]
for i in a:
    x = math.prod(a)
print(x)