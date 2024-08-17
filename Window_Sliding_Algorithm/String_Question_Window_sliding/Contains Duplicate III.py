from sortedcontainers import SortedList
a=[1,2,3,1,4,5,3,2,6]
n=9
k=3
# Window Sliding Algorithm K 
# for i in range(k):
#     l.append(a[i])
def max_arr(a,n,k):
    l=a[:k] #Found K sized array
    s=SortedList(l)
    # print(s[-1],end=' ') #Fetched Last value
    m=[] #Initialize lists
    m.append(s[-1])
    # print(s)
    for i in range(0,n-k): # loop till n-k size 9-3=6
        s.discard(a[i]) #0,1
        s.add(a[i+k]) #i=0 k=3 i+k=3 a[3]
        # print(s[-1],end=' ') #3,4,5,5
        m.append(s[-1])
    return m

print(max_arr(a,n,k))
# s=SortedList(a) 

a=[-100.5,30.465,-1.22,20.15]
import math
a.insert(1,-100.5)
a.pop(0)
a.sort()
# print(math.factorial(573.47))
i=-5.47e12
print(type(i))
# print(math.ceil(math.fabs(a[0])))
import re
s="Air Asia Airline 0047"
x=int(47)
print(x==47)
s="Aryan"
# ticket_data.py:- ticket_data=[]
# ticket_get_data()

# logic.py:- 







