s=input()
c1=c2=0
for i in s:
      if(i.islower()):
            c1=c1+1
      elif(i.isupper()):
            c2=c2+1
print("No. of Upper case characters :",c1)
print("No. of Lower case Characters :",c2)
