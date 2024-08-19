def rec(n):
    if(n==3):
        return 3
    if(n==0):
        return 1
    if(n==1):
        return 3
    return 3*rec(n//3)
    