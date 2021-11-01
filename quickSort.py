import random
import funcRunTime

#Generating array of random integers 0 to size
def generateArray(size):
    array = [random.randint(0, size+1) for _ in range(size)]
    return array  

@funcRunTime.timer #decorator used for time count
def quickSort(array, l, r):
    if l>=r:
        return
    
    pivot = array[r]
    i=l
    j=r-1

    while(i<=j):
        if array[i]>pivot:
            print('b', array)
            array[i],array[j]=array[j],array[i]
            print('a', array)
            j-=1
        else:
            i+=1
    
    m=j+1
    array[r],array[m]=array[m],array[r]

    quickSort(array, l, m-1)
    quickSort(array, m+1, r)

size = int(input("Enter size of the array: "))
array=generateArray(size)

print("Array before sort: ", array, sep='\n')
quickSort(array, 0, len(array)-1)

print("\nArray after Quick Sort: ", array, sep='\n')

print("\nTime: ", funcRunTime.timeNeeded)