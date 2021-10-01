import random
import time

def countingSort(array , n , position):

    #find maximum element in array
    Max = max(array) 

    # count array of size 10 (because 0 to 9) and with all elements 0
    count = (10)*[0]  

    # final array with all element 0 and size of main array
    farray = n*[0] 
    
    # find number of repeating elemets
    for i in array:
        count[(i // position) % 10] += 1

    # final index of count array
    c = 1
    while c < 10:
        count[c] += count[c - 1]
        c += 1
    
    #positionitioning of elements in  final array
    for i in range(n-1 , -1 , -1):
        farray[count[(array[i] // position) % 10] - 1] = array[i]
        count[(array[i] // position) % 10] -= 1
        
    #updates the main array
    for i in range(n):
        array[i] = farray[i]

def radixSort(array):
    Max = max(array)
    L = 1
    while Max // L > 0:
        countingSort(array , len(array) , L)
        L *= 10

#Driver code:
array = []
#input random values in array
for i in range(10):
    array.append(random.randint(1 , 100))
print("GIVEN ARRAY IS: ", array)
# count run time
t1 = time.time()
radixSort(array)
t2 = time.time()
# print("time taken for 10000 elements is: ", t2-t1, "sec")
# print("time taken in microseconds is: ", (t2-t1)*1000000, "micro sec")
print("SORTED ARRAY IS: ", array)
