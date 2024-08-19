target = [1,2,3,6,1]
target = [3,1,1,2]
target = [3,1,5,4,2]
# target = [3,1,5,2,4]
# target=[1,2,3,2,1,9,9,8,1,8,8,9]
target=[1,2,3,2,1,9,10,8,5,7,6,5,6,7,1,8,5,9]
#5-2+1=4+1
# 5 -1=4+1 5 
n=len(target)
# target.sort()
a=[1]*n
c=1
# 1,1,1,1,1
i=j=0
k=0
x=0
a=[]
# target = [3,1,5,4,2]
# 9 5 8  4 0 3

def reduce_len(a,n):
    # n=len(a)
    # while(n>1):
    if(a):
        m=min(a)
        j=0
        for i in range(n):
            a[i]=a[i]-m+1
        print(a,'reduce_len')
    subset(a,0)
        # k=0
        # while(k<n and a[k]!=1):
        #     k+=1
        # a=a[:k]
        # n=len(a)
        # print(a,'aa')
        # print(k,'kk')

def subset(a,i):
    k=i
    j=0
    n=len(a)
    if(sum(a)==n):
        return 1
    while(k<n and a[k]!=1):
        k+=1
        # i=ki
    l=a[i:k]
    n=len(l)
    print(l)
    # reduce_len(l,n)
    return subset(l,0)
while(i<n):
    # k=i
    j=i
    if(target[i]!=1):
        i=subset(target,i)
    i+=1
# print(c)
# print(reduce_len())