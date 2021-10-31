import random
import funcRunTime


def generateArray(n):
    array = [random.randint(0, n) for _ in range(n)]
    return array

def sortArray(arr):
    return sorted(arr)

@funcRunTime.timer
def binarySearch(arr, key):
    if(len(arr)<1):
        return -1
    m=len(arr)//2

    if(arr[m]==key):
        return m
    elif(arr[m]<key):
        return binarySearch(arr[m+1:], key)
    else:
        return binarySearch(arr[:m], key)

n = int(input("Enter size of the array: "))
arr=sortArray(generateArray(n))

key = int(input("Enter a number to search: "))

# print(arr)
result = binarySearch(arr, key)

if result<0:
    print("Key={} not found".format(key))
else:
    print("Key={} found at index={}".format(key,result))

print("Time: ", funcRunTime.timeNeeded)