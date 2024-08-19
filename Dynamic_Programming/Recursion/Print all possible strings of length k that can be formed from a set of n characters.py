def printAllKLengthRec(set, prefix, n, k):
    if (k == 0):
        print(prefix,'Prefix')
        return
    # print(prefix,'Outer_Loop')
    for i in range(n):
        newPrefix = prefix + set[i]
        print(newPrefix,prefix,i,k,'for loop')
        printAllKLengthRec(set, newPrefix, n, k - 1)
set1 = ['a', 'b']
k = 3
# printAllKLengthRec(set1,"",len(set1), k)
# print(1 or 2)
# aryan








