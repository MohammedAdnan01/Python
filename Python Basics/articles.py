para=list(input().split(" "))
articles=["The","the","A","a","an","An"]
words=[]
for i in range(len(para)):
    if para[i] in articles:
        words.append(para[i+1])
if words:
    print(words)
else:
    print(-1)
