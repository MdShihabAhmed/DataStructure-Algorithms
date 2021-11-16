import random
import funcRunTime

#Generating array of random integers -size to size
def generateArray(size):
    array = [random.randint(-size, size+1) for _ in range(size)]
    return array

@funcRunTime.timer #decorator used for time count
def maximum_subarray(array):
    
    size = len(array)
    maximum=float('-inf')
    a=array

    for i in range(size):
        subarraysize=i+1
        for j in range(size):
            if(j+subarraysize>size):
                break
            summ=sum(array[j:j+subarraysize])
            if(summ>maximum):
                arr=array[j:j+subarraysize]
                maximum=summ
    
    return arr,maximum

size = int(input("Enter size of the array: "))
array=generateArray(size)

print("Array: ", array, sep='\n')
arr,maximum=maximum_subarray(array)

print("\nMaximum subarray: ", arr, sep='\n')
print("\nMaximum subarray sum: ", maximum, sep='\n')

print("\nTime: ", funcRunTime.timeNeeded)