nums = [0,1,1,3]
maximumBit = 2
# nums = [2,3,4,7]
# maximumBit = 3


l=[]

a=[]
a=[nums[0]]
for i in range(1,len(nums)):
    a.append(a[i-1]^nums[i])
print(a)
k=2**maximumBit-1
while(a):
    l.append(a[-1]^k)
    a.pop()

print(l)