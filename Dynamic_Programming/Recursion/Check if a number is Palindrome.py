n=1232
s=str(n)
n=len(s)
l=0
r=n-1
def rec(s,l,r):
    if(l==r):
        return True
    if(s[l]!=s[r]):
        return False
    return rec(s,l+1,r-1)
print(rec(s,l,r))
