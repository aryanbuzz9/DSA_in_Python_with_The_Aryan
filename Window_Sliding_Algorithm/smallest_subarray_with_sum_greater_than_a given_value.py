def smallest_length(a,x,n):
    start=0
    end=0
    window_sum=0    
    min_length=n+1
    if(a[0]>x):
        return 1
    while(end<n):               
        # fetching sum >= x
        while(window_sum<=x and end<n):
            window_sum=window_sum+a[end]
            end+=1
        while(window_sum>x): #if window_sum>x then length will be reduced
            if(end-start<min_length): #and first remove value from window_sum
                min_length=end-start  #To find length
            window_sum=window_sum-a[start] #Remove values from starting
            start+=1 

    return min_length

#The Aryan Code
a=[1,4,45,6,10,19]
x=51
n=len(a)
print(smallest_length(a,x,n))



        
