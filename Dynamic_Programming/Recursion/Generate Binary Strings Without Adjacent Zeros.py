
def validStrings(n):
    # 111 110 101 011 010
    # 1111 5 0110 1010 0101
    binary_str=['0','1']
    k=2
    rec('',n,k,[],binary_str)
    # print(l)
    # return [/]
def rec(s,n,k,a,binary_str):
    if('00' in s):
        return
    if(n==0):
        a.append(s)
        # print(a)
        # return a
    else:
        for i in range(k):
            s1=s+binary_str[i]
            # if(i==3)
            # c=c+1
            rec(s1,n-1,k,a,binary_str)
    return a
n=3
binary_str=['0','1']
# print(validStrings(n))


print(rec('',n,2,[],binary_str))


def validStrings(n,s,res):
    if res is None:
        res = []
    # if '00' in s:
    #     return
    if n == 0:
        res.append(s)
    else:
        validStrings(n - 1, s + 'a', res)
        validStrings(n - 1, s + 'b', res)
    
    return res 

# print(validStrings(3,'',[]))