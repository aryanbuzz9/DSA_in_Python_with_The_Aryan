#Find Subarray with given Sum from Array of non-negative Numbers
def subarray(a,x,n):
    window_sum=a[0]
    if(window_sum==x):
        return 1
    i=1
    j=0
    while(i<n):
        #iterate till window_sum < x
        while(window_sum<x and i<n): 
            window_sum=window_sum+a[i]
            i+=1
        #remove the value from starting index
        while(window_sum>x and j<n): 
            window_sum=window_sum-a[j] 
            j+=1
        if(window_sum==x):
            return j+1,i
    if(i==n): # if i reaches to the end index means no subararr found...
        return -1
a=[15, 2, 4, 8, 9, 5, 10, 23]
# a=[2,3,4,56,24]
x=23
n=len(a)
print(subarray(a,x,n))
