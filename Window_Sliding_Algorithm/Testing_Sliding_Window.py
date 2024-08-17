from collections import defaultdict
s="bcabbcaabbccacacbabccacaababcbb"
words=["c","b","a","c","a","a","a","b","c"]
# s="barfoofoobarthefoobarman"
# words=["bar","foo","the"]
s="aaaaaaaaaaaaaa"
words=['aa','aa']
# s="lingmindraboofooowingdingbarrwingmonkeypoundcake"
# words=["fooo","barr","wing","ding","wing"]
# s="ababaab"
# words=["ab","ba","ba"]
# s="mississippi"
# words=["si","is"]
n=len(s)
w_len=len(words[0])
d=defaultdict(int)
d1=defaultdict(int)
d3=defaultdict(int)
for i in words:
    d3[i]+=1
# print(d3)
i=j=c=count=0
wlen=len(words)
s1=''
j=1
c=0
x=''
k=m=0
b=w_len*wlen
# s="wordgoodgoodgoodbestword"
ind=0
a=[]
s2=[]
print(n)
l=[]
# s="bcabbcaabbccacacbabccacaababcbb"
# words=["c","b","a","c","a","a","a","b","c"]
print(d3)
x=1
x1=0
t=0
# s="mississippi"
for i in range(0,n-b+1):
    j=i
    d=defaultdict(int)
    for j in range(i,b+i,w_len):
        # s2.append(s[i])
        l.append(i)
        s1=s[j:j+w_len]
        print(s1,i)
        # print(s1)
        if(s1 in words):
            d[s1]+=1
            if(d[s1]<=d3[s1]):
                # d1[s1]=i
                # d1[s1]=min(l)
                
                print(i,d[s1],s1,count,"here",x1)
            
            else:
                break
        else:
            break
        j=j+w_len
    else:
        a.append(i)
        
    # i+=1
    
# a=set(a)
# a=list(a)
# a.sort()
print(a)
