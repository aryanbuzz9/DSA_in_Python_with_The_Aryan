n=8
a=[1 for i in range(1,n+1)]
# 1 2 3 4 5 6 7 8
prefix_arr=[i for i in range(n+1)]
prefix_sum=sum(prefix_arr)
left=0
right=prefix_sum-left
c=0
# if(n==1):
#     return 1
for i in range(1,n+1):
    if(left==right):
        c=i-1
        print(left,right)
    left+=prefix_arr[i-1]
    right-=prefix_arr[i]
print(c)