from collections import defaultdict
garbage = ["G","P","GP","GG"]
travel = [2,4,3]
# garbage = ["MMM","PGM","GP"]
# travel = [3,10]
s=set(''.join(garbage))
# print(garbage_len)
# ['G','P']
first=set(garbage[0])
count=0
# for i in range(len(garbage[0])):
#     if('G' in garbage[0]):
#             count+=garbage[0].count('G')
d={}
for i,j in enumerate(garbage):
    if('G' in j):
        count+=j.count('G')
        d['G']=i
    if('P' in j):
        d['P']=i
        count+=j.count('P')
    if('M' in j):
        d['M']=i
        count+=j.count('M')
# for i,j in enumerate(garbage):
#     if('G' in j):
#         # count+=i.count('G')
#         # if('G' in first):
#         d['G']=i
#     if('P' in j):
#         d['P']=i
#         # count+=i.count('P')
#     if('M' in j):
#         d['M']=i
        # count+=i.count('M')
print(d)
if('G' in s):
    count+=sum(travel[0:d['G']])
if('P' in s):
    count+=sum(travel[0:d['P']])
if('M' in s):
    count+=sum(travel[0:d['M']])
print(count)


# for i in range(1,len(garbage)):
#     if('G' in garbage[i]):
#         count+=garbage[i].count('G')
    # else:





