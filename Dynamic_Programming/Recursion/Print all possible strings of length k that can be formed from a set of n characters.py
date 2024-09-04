def printAllKLengthRec(set, prefix, n, a,k):
    if('00' in prefix):
        return
    if (k == 0):
        # print(prefix,'Prefix')
        a.append(prefix)
    else:
        for i in range(n):
            newPrefix = prefix + set[i]
            # print(newPrefix,prefix,i,k,'for loop')
            printAllKLengthRec(set, newPrefix, n, a,k - 1)
    return a
set1 = ['0', '1']
k = 3

l=printAllKLengthRec(set1,"",len(set1),[], k)
print(l)
# print(1 or 2)
# aryan








