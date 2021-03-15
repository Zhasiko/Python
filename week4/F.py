"""
Дан файл инпута, надо считать строки и вывести йес, 
если каждая послед строка длиннее предыдущей, иначе ноу, и вывод в файл аутпута сделать
"""
input = open("input.in","r")
output = open("output.in","w")
file = input.read().split("\n")
a = list()
for i in file:
    a.append(len(i))
for i in range(1,len(a)):
    if a[i]<=a[i-1]:
        print("No",file=output,end="")
        exit()
print("Yes",file=output,end="")