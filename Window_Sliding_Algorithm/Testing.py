from collections import defaultdict
d=defaultdict(lambda :0)
d1=defaultdict(lambda :0)

s="xyzzaz"
# s="aababcabc"
s="xyzzazzaxyzashfrgfehgyfrgdshfgdsugfdshfdsfh"
n=len(s)
count=c=i=j=0
while(i<n):
    d[s[i]]+=1
    if(d[s[i]]==1):
        d1[s[i]]=i
        count+=1
    else:
        ind=d1[s[i]]
        count=0
        d=defaultdict(lambda :0)
        i=ind
        j=i+1
    if(count==3):
        c+=1
        count-=1
        # d[s[i]]-=1
        d[s[j]]=0
        j=j+1
    i+=1
print(c)