# To find the maximum sum of all subarrays of size K
a=[100,200,300,400]
n=len(a)
k=2
def sub_array(a,k):
    window_sum=sum(a[:k])
    for i in range(n-k):
        current_sum=window_sum-a[i]+a[k+i]
        window_sum=max(window_sum,current_sum)
    return window_sum
print(sub_array(a,k))






