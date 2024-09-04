nums = [2,3,7,5,10]
# total_sum=0
s=nums[0]
max_sum=s
total_sum=s+max_sum
a=[total_sum]
for i in range(1,len(nums)):
    current_sum=nums[i]
    max_sum=max(max_sum,current_sum)
    total_sum+=current_sum+max_sum
    a.append(total_sum)
print(a)