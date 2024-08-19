from collections import defaultdict
d=defaultdict(int)
s = "RLRRLLRLRL"
s = "RLRRRLLRLL"
s="LLLLRRRR"
total_count=0
r_count=l_count=0
for i in s:
    if(i=='R'):
        r_count+=1
    if(i=='L'):
        l_count+=1
    if(r_count==l_count):
        total_count+=1
print(total_count)
