b = [23,11,42,3,12]


print(b)


def insertSort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j>=0 and a[j]<key:
            a[j+1] = a[j]
            j=j-1
        a[j+1] = key

insertSort(b)


print(b)
