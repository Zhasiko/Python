"""
дано слово и некий символ, который является "точкой выхода",
нужно вывести лист с расстояниями всех других символов до ближайшей точки выхода
"""
import re
s = str(input())
s1 = str(input())
a = list()
for i in range(len(s)):
    if i == 0:
        x = re.search(s1,s)
        a.append(x.start())
        continue
    if i == len(s)-1:
        x = re.search(s1,s[::-1])
        a.append(x.start())
        continue
    x = re.search(s1,s[i::-1])
    y = re.search(s1,s[i+1:])
    if x and y:
        a.append(min(x.start(),y.start()+1))
        continue
    if x:
        a.append(x.start())
        continue
    if y:
        a.append(y.start()+1)
        continue
print(a)