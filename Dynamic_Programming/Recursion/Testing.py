n=3
def rec(n,c):
    if(n==0):
        print(c)
        return
    for i in range(2):
        c=c+1
        print(i,n,'index',c)
        rec(n-1,c)
# print(rec(n,0))
# 3 rec(0) 4 rec (1)  rec(2) rec(3)
# rec(0):- rec(1) 4
# rec(2):- 
def rec(n):
    if(n==0):
        return
    for i in range(2):
        print(i,n)
        rec(n-1)
rec(3)
# rec(3) rec(2) rec(1)
# 3 2 1 2 1



  








