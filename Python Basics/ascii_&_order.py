s = 'Adnan15973'
sum=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
    if i.isalpha():
        sum+=ord(i)
print(sum)
