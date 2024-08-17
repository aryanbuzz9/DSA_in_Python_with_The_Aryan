a=[ -2, -1, -2, -4, 3 ]
count_neg=max_neg=-10**8
for i in a:
    if(i<0):
        count_neg+=1
        max_neg=max(max_neg,i)
# del a[max_neg]
mul=1
for i in a:
    mul*=i
if(count_neg%2==0):
    print(mul//max_neg)
elif(len(a)==2):
    print(min(a))
else:
    print(mul)
print(29*3,26*5,21*6)


