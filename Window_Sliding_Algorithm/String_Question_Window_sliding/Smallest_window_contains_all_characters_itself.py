

from collections import defaultdict
s='aabcbcdbca'
n=len(s)
d=defaultdict(lambda :0)
dist_count=len(set(s))
i=0
j=0
# print(d)
count=0
l=n+1
start=0
for i in range(n):
    d[s[i]]=d[s[i]]+1
    print(d,i)
    # print(d[s[i]])
    if(d[s[i]]==1):
        count+=1
        # print(d,'count',count,i)
    if(count==dist_count):
        while(d[s[j]]>1):
            if(d[s[j]]>1):
                d[s[j]]=d[s[j]]-1
            
            j+=1
            print(d,'while',j)
        if(l>i-j+1):
            l=i-j+1
            start=j

print(start)   
print(str(s[start:start+l]))
print(l)
# s[0]=a | d[a]=1
# s[1]=a | d[a]=1+1=>2

# print(d)