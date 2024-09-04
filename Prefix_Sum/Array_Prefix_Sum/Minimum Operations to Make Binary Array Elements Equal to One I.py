nums = [0,1,1,1,0,0]
n=len(nums)
a=nums[:3]
k=3
for j in range(k):
    if(a[j]==0):
        a[j]=1
    else:
        a[j]=0
print(a)
d={0:1,1:0}
print(d)
# [0,1,1,1,0,0]
# 1 0 0 1 0 0
# 1 1 1 0 0 0
#  1 1 1 1 1 1
for i in range(n-k+1):
    # a=nums[i:i+k]
    for j in range(i,i+k):
        if(nums[j]==0):
            nums[j]=1
        else:
            nums[j]=0
print(nums)

    
    