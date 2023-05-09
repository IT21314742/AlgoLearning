A =[]
for v in range(1,8):
    number = int(input("Enter Number  : "))
    A.append(number)

print("usorted Array :",A)
print(len(A))
def selectionSort(A):
    n= len(A)
    for i in range(0,n-1):
        smallest = i
        for j in range(i+1,n):
            if(A[j] < A[smallest]):
                smallest = j
            A[i],A[smallest] = A[smallest],A[i]

selectionSort(A)
print("Sorted Arrray : ",A)
