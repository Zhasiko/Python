"""
даны два массива с числами, и некое число. 
Крч надо вывести колво элементов с одинаковыми индексами, 
в интервал которых входит это некое число
"""
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = int(input())
cnt=0
for i,j in zip(a,b):
    if j-i<=c:
        cnt+=1
print(cnt)