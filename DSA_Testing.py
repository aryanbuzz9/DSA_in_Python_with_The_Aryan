from itertools import permutations
l = list(permutations(range(1, 4),2))
# print(l[0])
for j in l:
    print(j,len(j))
    # search_cost=0
    # max_val=-1
    for i in range(len(l[0])):
        print(i)
        # if(max_val<j[i]):
        #     max_val=j[i]

