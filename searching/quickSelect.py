from random import randint


class ExtendedSolution:
    def partition(self, array, left, right, partition_index):
        # pick pivot number as the partition point of the list
        pivot_number = array[partition_index]

        # Move pivot to end
        self.swap(array, partition_index, right)

        partition_index = left
        for i in range(left, right):
            if array[i] <= pivot_number:
                self.swap(array, i, partition_index)
                partition_index += 1

        self.swap(array, partition_index, right)

        return partition_index

    def quickSelect(self, array, left, right, k):
        # If the list contains one element, return that element
        if left == right:
            return array[left]

        # Select partition between left and right
        partition_index = randint(left, right)
        partition_index = self.partition(array, left, right, partition_index)

        # Now that we've paritioned, check results
        # If the partition is at k
        if k == partition_index:
            return array[k]
        elif k < partition_index:
            return self.quickSelect(array, left, partition_index - 1, k)
        else:
            return self.quickSelect(array, partition_index + 1, right, k)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]


class ConciseSolution:
    def quickSelect(self, array, left, right, k):
        p_index, pivot_number = left, array[right]
        for i in range(left, right):
            if array[i] <= pivot_number:
                self.swap(array, i, p_index)
                p_index += 1

        self.swap(array, p_index, right)

        if k == p_index:
            return array[k]
        elif k < p_index:
            return self.quickSelect(array, left, p_index - 1, k)
        else:
            return self.quickSelect(array, p_index + 1, right, k)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]


array = [7, 4, 6, 3, 9, 1]
k = 2 
s = ConciseSolution()
print(s.quickSelect(array, 0, len(array) - 1, len(array) - k))