#Updated on 21-07-24 08:34am Sunday
def smallest_length(a,x,n):
    start=0
    end=0
    window_sum=0
    min_length=n+1
    l=a[:]
    j=0
    if(a[0]>x):
        return 1
    if(sum(a)<x):
        return 0
    while(end<n):            
        # fetching sum >= x
        while(window_sum<=x and end<n):
            window_sum=window_sum+a[end]
            # l.append(a[j])
            end+=1
        while(window_sum>x): #if window_sum>x then length will be reduced
            if(end-start<min_length): #and first remove value from window_sum
                min_length=end-start  #To find length
                l.remove(a[j]) #To find array having smallest length
                j+=1
            window_sum=window_sum-a[start] #Remove values from starting
            start+=1 
    l.insert(0,a[j-1]) # Values will be removed from l till length-1, So
                        #insert value at 1st position
    return min_length,l[:min_length]

#The Aryan Code
# a=[1,4,45,59,10,19]
a=[1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
x=51
x=280
n=len(a)
print(smallest_length(a,x,n))



        
