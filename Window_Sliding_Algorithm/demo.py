# Python 3 implementation to find the length of 
# longest increasing contiguous subarray


# function to find the length of longest 
# increasing contiguous subarray
def lenOfLongIncSubArr(arr, n) :

	# 'max' to store the length of longest
	# increasing subarray
	# 'len' to store the lengths of longest
	# increasing subarray at different 
	# instants of time
	m = 1
	l = 1
	
	# traverse the array from the 2nd element
	for i in range(1, n) :

		# if current element if greater than previous
		# element, then this element helps in building
		# up the previous increasing subarray encountered
		# so far
		if (arr[i] > arr[i-1]) :
			l =l + 1
		else :

			# check if 'max' length is less than the length
			# of the current increasing subarray. If true, 
			# then update 'max'
			if (m < l) :
				m = l 

			# reset 'len' to 1 as from this element
			# again the length of the new increasing
			# subarray is being calculated 
			l = 1
		
		
	# comparing the length of the last
	# increasing subarray with 'max'
	if (m < l) :
		m = l
	
	# required maximum length
	return m

# Driver program to test above
arr = [1,2,3,4,5,6]
n = len(arr)
c=0
k=m=1
l=[1]
for i in range(n-1):
    s=str(i)
    for j in range(i+1,n):
        s=s+str(j)
        t=len(s)
        if((n//2)>j):
            if(t>m and t<n//2 and t>l[c]):
                m=t
                c=c+1
                l.append(t)
                k=k+1
        else:
            c=c-1
            m=min(l)
            break
print(k+1)


# This code is contributed
# by Nikita Tiwari.
