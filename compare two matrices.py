n,m=map(int,input().split())
a=[[int(input())for i in range(n)]for j in range(m)]
o,p=map(int,input().split())
b=[[int(input())for i in range(o)]for j in range(p)]
def compare(a,b):
    if n==o and m==p:
        for i in range(n):
            for j in range(m):
                if a[i][j]==b[i][j]:
                    return True
                else:
                    return False
    else:
        return False
print(compare(a,b))
