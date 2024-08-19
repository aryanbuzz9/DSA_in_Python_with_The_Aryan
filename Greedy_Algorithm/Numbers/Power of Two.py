import math
n=64
sqrt=int(math.sqrt(n))+2
# print(sqrt)
for i in range(1,sqrt):
    if(2**i==n):
        # print("Y")
        break
#Using Recursion

print(n)
def rec(n):
    if(n==1):
        return 2
        # return True
    if(n==2):
        return 2
    if(n==0):
        return 1
    return 2*rec(n//2)
print(rec(n))