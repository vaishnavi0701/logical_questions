
d1={'a':100 , 'b': 200 , 'c' : 300}
d2={'a':200,  'b':300,  'd':400}
d3={}
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=(j+y)
# print(d3)
d4={}
for k in (d1,d2,d3,d4):
    d4.update(k)
print(d4)
