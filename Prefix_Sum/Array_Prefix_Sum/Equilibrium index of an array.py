a=[7,2,1,5]
prefix_sum=sum(a)
n=len(a)
left=a[0]
for i in range(1,n):
    w=prefix_sum-a[i]
    right=w-left
    if(left==right):
        print("Yes")
        break
    else:
        left+=a[i]