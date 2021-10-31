import random
import funcRunTime

#Generating array of random numbers 0 to n
def generateArray(n):
    array = [random.randint(0, n+1) for _ in range(n)]
    return array  

@funcRunTime.timer #decorator used for time count
def mergeSort(arr):
    if len(arr)<=1:
        return

    m=len(arr)//2
    f=arr[:m]
    l=arr[m:]

    # print('Dividing: ', arr)
    mergeSort(f)
    mergeSort(l)

    i=j=k=int(0)
    while i<len(f) and j<len(l):
        if f[i]<l[j]:
            arr[k]=f[i]
            i+=1
        else:
            arr[k]=l[j]
            j+=1
        k+=1
    
    while i<len(f):
        arr[k]=f[i]
        i+=1
        k+=1
    
    while j<len(l):
        arr[k]=l[j]
        j+=1
        k+=1
    
    # print('Sorted Combining: ',arr)

n = int(input("Enter size of the array: "))
arr=generateArray(n)

# print("Array before sort: ", arr, sep='\n')
mergeSort(arr)

print("\nArray after Merge Sort: ", arr, sep='\n')

print("\nTime: ", funcRunTime.timeNeeded)