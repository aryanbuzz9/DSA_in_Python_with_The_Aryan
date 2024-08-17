# written on 21-07-24 10:02 Sunday
def subarray(a,k,n):
    sub=a[:k] # get subarray of k length
    window_max=max(sub) 
    print(window_max,end=' ')
    for i in range(n-k): # n=9 ,k=3 n-k=6
        window_max=max(window_max, a[i+k]) #compare with i+k element
        # window_max=max(current_max,window_max)
        print(window_max,end=' ')
a=[1, 2, 3, 1, 4, 5, 2, 3, 6]
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k=3
n=len(a)
print(subarray(a,k,n))
