import re

txt = input()
x = re.split("[.,]", txt)
for i in x:
    print(i)

