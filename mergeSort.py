import random
import funcRunTime

#Generating array of random integers 0 to size
def generateArray(size):
    array = [random.randint(0, size+1) for _ in range(size)]
    return array  

@funcRunTime.timer #decorator used for time count
def mergeSort(array):
    if len(array)<=1:
        return

    mid=len(array)//2
    firstHalf=array[:mid]
    lastHalf=array[mid:]

    # print('Dividing: ', array)
    mergeSort(firstHalf)
    mergeSort(lastHalf)

    i=j=k=int(0)
    while i<len(firstHalf) and j<len(lastHalf):
        if firstHalf[i]<lastHalf[j]:
            array[k]=firstHalf[i]
            i+=1
        else:
            array[k]=lastHalf[j]
            j+=1
        k+=1
    
    while i<len(firstHalf):
        array[k]=firstHalf[i]
        i+=1
        k+=1
    
    while j<len(lastHalf):
        array[k]=lastHalf[j]
        j+=1
        k+=1
    
    # print('Sorted Combining: ',array)

size = int(input("Enter size of the array: "))
array=generateArray(size)

# print("Array before sort: ", array, sep='\n')
mergeSort(array)

print("\nArray after Merge Sort: ", array, sep='\n')

print("\nTime: ", funcRunTime.timeNeeded)