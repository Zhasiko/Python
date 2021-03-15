"""
 дано н строк, каждая состоит из 3 слов, нужно вывести дикшнари 
 где a = колво прописных букв в первых словах, 
 b = колво гласных во вторых словах, c = колво цифр в 3 словах
"""
n = int(input())
cntU,cntV,cnt = 0,0,0
m = dict()
for i in range(n):
    s = input().split()
    for i in s[0]:
        if 'A'<=i<='Z':
            cntU+=1
    for i in s[1]:
        if i.lower() in "aeoiu":
            cntV+=1
    for i in s[2]:
        if i in "0987654321":
            cnt+=1
m["a"]=cntU
m["b"]=cntV
m["c"]=cnt
print(m)