nums = [10,4,8,3]
# n=len(a)
left=0
prefix_sum=sum(nums)
right=prefix_sum-nums[0]
diff=abs(right-left)
prefix_arr=[]
prefix_arr.append(diff)
for i in range(1,len(nums)):
    left+=nums[i-1]
    right=right-nums[i]
    diff=abs(right-left)
    prefix_arr.append(diff)
    # left=nums[i]/
print(prefix_arr)