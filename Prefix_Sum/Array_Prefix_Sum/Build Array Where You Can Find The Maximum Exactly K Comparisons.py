
max_ind=-1

# n=len(arr)
n = 2
m = 3
k = 1
# n = 5
# m = 2
# k = 3
n = 9
m = 1
k = 1
n=50
m=100
k=25
# extra_a=[]
# for i in range(1,m+1):
    
#     extra_a.append([i,i])
# print(extra_a)
# m_arr=[i for i in range(1,m+1)]
from itertools import permutations
a = list(permutations(range(1, m+1),n))
c=0

for i in range(1,m+1):
    t=[]
    for j in range(i,n+1):
        t.append(i)
    a.append(t)
    # a.append([i,i])
# print(a)
for j in a:
    search_cost=0
    max_val=-1
    for i in range(len(j)):
        if(max_val<j[i]):
            max_val=j[i]
            # print(j[i],end=' ')
            search_cost+=1
    # print()
    if(search_cost==k and j[i]<=m):
        c+=1
print(c)