piles =[2,4,5]
piles=[9,8,7,6,5,1,2,3,4]
# piles=[2,4,1,2,7,8]
# piles=[2,4,1,2,7,8,4,5,6,10,11,12]
n=len(piles)
n_3=n//3
piles.sort()
# 1 2 2 4 7 8
total_sum=0
print(n_3)
print(piles)
for i in range(n_3,n-1,2):
    total_sum+=piles[i]
    # n_3+=n_3
print(total_sum)