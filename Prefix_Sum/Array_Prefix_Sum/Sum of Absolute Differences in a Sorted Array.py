nums = [1,4,6,8,10]
nums = [2,3,5]
nums=[2,3,5,8,10,16,21]
nums=[2,3,5,10,15,20]
n=len(nums)
l=[]
# print(sum(nums))
# [51,46,40,37,39,57,82]
# 
# nums.sort()
# [2,3,5,10,15,20]
# [43,39,35,35,45,65]
a=[1,3,8,13,18]
# 5+10+15
# 2+7+12+17
diff=nums[1]-nums[0]
for i in range(n):
    s=0
    # ind=diff
    if(i==0):
        ind=0
    elif(i==1):
        ind=diff
    else:
        ind=nums[i]-nums[i-1]+a[i-1]
        print(ind)
    for j in range(i+1,n):
        s=s+abs(nums[i]-nums[j])
    l.append(s+ind)
print(l)

