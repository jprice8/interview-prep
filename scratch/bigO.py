# Nested loop trickery

def printUnorderedArray(array):
    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            print(f'{array[i]} {array[j]}')        

            j += 1

        i += 1


printUnorderedArray(array=[1, 2, 3, 4])