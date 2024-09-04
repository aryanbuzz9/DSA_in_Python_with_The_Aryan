ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5

# ranges = [[1,2],[3,3],[8,10]]
# left = 2
# right = 8
a=[i for i in range(left,right+1)]
print(a)
# 2 3 4 5
n=right-left+1
# i=0
j=c=0
flag=False
# ranges.s
for i in ranges:
    # print(i[1])
    while(j<n and i[1]>=a[j] and i[0]<=a[j]):
        c+=1
        j+=1
    if(c==n):
        flag=True
        break
print(flag)
if(flag):
    print("Yes")
else:
    print("No")




