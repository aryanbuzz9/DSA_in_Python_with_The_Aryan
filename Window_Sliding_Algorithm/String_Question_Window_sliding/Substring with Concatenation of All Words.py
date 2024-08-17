from collections import defaultdict
s="bcabbcaabbccacacbabccacaababcbb"
words=["c","b","a","c","a","a","a","b","c"]
# s="barfoofoobarthefoobarman"
# words=["bar","foo","the"]
# s="aaaaaaaaaaaaaa"
# words=['aa','aa']
s="lingmindraboofooowingdingbarrwingmonkeypoundcake"
words=["fooo","barr","wing","ding","wing"]
# s="ababaab"
# words=["ab","ba","ba"]
s="mississippi"
words=["si","is"]
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
l=[0]
# s="bcabbcaabbccacacbabccacaababcbb"
# words=["c","b","a","c","a","a","a","b","c"]
print(d3)
x=0
x1=0
t=0
# s="mississippi"
while(i<n):
    s2.append(s[i])
    l.append(i)
    if(j==w_len):
        s1=''.join(s2)
        print(s1,i)
        # print(s1)
        
        if(s1 in words):
            d[s1]+=1
            # print(s1)
            s2=[]
            j=0
            if(d3[s1]>1 and d[s1]<=d3[s1]):
                # d1[s1]=i
                d1[s1]=min(l)
                count+=1
                x1=min(l)
                print(i,d[s1],s1,count,"here",x1)
            elif(d[s1]==1):
                d1[s1]=i
                count+=1
                x1=min(l)
                
                l=[]
                # print(d,i)
                m=i
            else:
                print(d1[s1],s1,'else d1')
                count=0
                t=t+1
                i=d1[s1]
                x=x+1
                i=t-1
                # i=abs(i-x)
                l=[]
                # i=x-1
                d=defaultdict(lambda :0)
                d1=defaultdict(lambda :0)
            if(count==wlen):
                ind=abs(i+1-b)
                a.append(ind)
                x=x+1
                t=t+1
                i=t-1
                # i=ind
                d=defaultdict(lambda :0)
                d1=defaultdict(lambda :0)
                print("Y",ind,i,x1)
                l=[]
                count=0
        else:
            # i=i-1
            j=j-1
            count=0
            x=x+1
            i=x-1
            # print(s2)
            d=defaultdict(lambda :0)
            d1=defaultdict(lambda :0)
            s2.remove(s2[0])
            l=[]
            t=t+1
            # ind=abs(i+1-b)
            i=ind


    i+=1
    j+=1
a=set(a)
a=list(a)
a.sort()
print(a)
