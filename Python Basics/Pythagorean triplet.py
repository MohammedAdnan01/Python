import math
a=[]
for i in range(1,21):
    a.append(i**2)
print(a)
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        c=a[i]+a[j]
        if a.count(c)==1:
            print(int(math.sqrt(a[i])),int(math.sqrt(a[j])),int(math.sqrt(c)))
            
