a=[1,0,0,1,-1,-1,0,0,1,-1]
n=len(a)
i=0
j=0
# count=0
max_len=-1
max_list=[]

while(j<n):
    m=[]
    count=0
    while(a[i]>=0):
        m.append(a[i])
        count+=1
        i+=1
        j=i
    j+=1
    if(max_len<count):
        max_len=count
        max_list=m
print(max_list,max_len)
