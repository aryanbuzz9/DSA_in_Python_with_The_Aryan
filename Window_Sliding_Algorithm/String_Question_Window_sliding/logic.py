c=0
nums=[1,2,3,4]
for i in nums:
    j=i
    while(i%3!=0 or j%3!=0):
        i-=1
        j+=1
        if(i%3!=0 or j%3!=0):
            c+=1
            break
        print(c)
print(c)