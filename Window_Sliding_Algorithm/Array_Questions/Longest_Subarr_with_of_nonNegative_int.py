def subarray(a,n):
    i=0
    # window_val=a[0]
    l=[]
    length=-1
    c=0
    m=[]
    while(i<n): 
        if(a[i]<0):
            if(length<c):
                length=c
                # assign list (l) to m with longest length
                m=l
            #l=[] because insertion will be started from beginning
            l=[]
            c=0
        else:
            l.append(a[i])
            c+=1
        i+=1
    return m,max(c,length)
# a=[2, 3, 4, -1, -2, 1, 5, 6, 3]
a=[1, 0, 0, 1, -1, -1, 0, 0, 1,-1]
n=len(a)
print(subarray(a,n))