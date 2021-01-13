rows,cols=map(int,input().split(" "))
print(rows,cols)
mat=[]
sum_of_diagonal=[]
for i in range(rows):
    temp=list(map(int,input().split(" ")))
    mat.append(temp)
print(mat)
for i in mat:
    print(" ".join(map(str,i)))

for i in range (rows):
    temp=mat[i][i]
    sum_of_diagonal.append(temp)
    b=sum(sum_of_diagonal)

print(b)
    

