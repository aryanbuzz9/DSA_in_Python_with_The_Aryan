nums = [1,0,1,0,1]
goal = 2
nums=[0,0,0,0,0]
goal=-1
n=len(nums)
# print(
c=0
# zero=list(set(nums)
i=0
c=0
s=0
j=0
while(i<n):
    # def until_goal(k,i):
    while(s<=goal):
        s=s+nums[i]
        # c+=1
        if(s==goal):
            c+=1
        i+=1
    while(s>goal):
        print(s)
        s=s-nums[j]
        if(s==goal):
            c+=1
        j+=1
    i+=1
    # print(nums[j:i])
    print(s,'lower')
    
    # i+=1
print(c)
