s='32'
s="82734"
# s='22'
l=[]
total=0
for i in s:
    s1=bin(int(i))
    print(s1)
    s1=int(s1[2:])
    # total+=1
    # print(s1)
    l.append(s1)
s_int=int(s)
w=0
# i=1
c=1
# print(s_int,l)
# for j in range(10):
#     for i in range(len(l)):
#         w=w+l[i]
#         if(w==s_int):
#             break
#         print(w)
#     c=c+1
#     if(w==s_int):
#         break
    
print(max(s))
    

