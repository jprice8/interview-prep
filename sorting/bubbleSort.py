import time

# O(n^2) time where n is the elements of the array | O(1) space
def bubbleSort(array):
    isSorted = False 
    while not isSorted:
        isSorted = True 
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    return array

# start_time = time.time()
# print(bubbleSort([4, 2, 3, 21, 1, 4, 5, 5, 5]))
# print("--- %s seconds ---" % (time.time() - start_time))

def optimizedBubbleSort(array):
    isSorted = False 
    counter = 0
    while not isSorted:
        isSorted = True 
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                isSorted = False 
        counter += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    return array


print(optimizedBubbleSort([6, 2, 3, 5, 5, 11, 2]))