from collections import defaultdict
a = [1,2,1,3,1]
k = 3
a=[1,0,1,1]
k = 1
a=[1,2,3,1,2,3]
k = 2
n=len(a)
d=defaultdict(int)
d1=defaultdict(int)
for i in range(n):
    if(a[i] not in d1):
        d1[a[i]]=i
print(d1,'d1')
l=[]
# a = [1,2,1,3,1]
for i in range(n):
    d[a[i]]+=1
    # d1[a[i]]=i
    if(d[a[i]]>1):
        j=d1[a[i]]
        l.append(i)
        d1[a[i]]=i
        # print(i,j,a[i],a[j])
        if(abs(i-j)<=k and a[i]==a[j]):
            print(True)
            break
        else:
            print(False)
        # print(abs(i-j),a[i],a[j])
        d1[a[i]]=i
print(l)




