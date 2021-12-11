i=1
a=[]
size=int(input("enter no of items"))
for i in range(size):
    val=int(input("enter the number"))
    a.append(val)
    i=i-1
print(a)
product=1
for i in range(size):
    product=product*a[i]
print(product)
    