
a="w3resource"
i=0
b=0
c={}
for i in a:
    if i not in c:
        c[i]=1
    else:
        c[i]=c[i]+1
print(c)