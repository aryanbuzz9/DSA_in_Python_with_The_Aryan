#https://leetcode.com/problems/sliding-subarray-beauty/

from sortedcontainers import SortedList
nums=[1,-1,-3,-2,1,2,3,4,5,-4,-4,-3,-2]
# s=SortedList()
k=4
x=2
a=nums[:k]
n=len(nums)
a=SortedList(a)
m=[]
if(a[x-1]>=0):
    m.append(0)
else:
    m.append(a[x-1])
i=0
while(i<n-k):
    a.add(nums[i+k])
    a.discard(nums[i])
    if(a[x-1]>=0):
        m.append(0)
    else:
        m.append(a[x-1])
    i+=1
print(m)