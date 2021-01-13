num=list(input())
value=0
for i in range(len(num)):
    digit=num.pop()
    if digit=='1':
        value=value+pow(2,i)
print(value)
