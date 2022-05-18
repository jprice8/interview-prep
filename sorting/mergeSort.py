class Solution:
    def mergeSort(self, arr):
        if len(arr) < 2:
            return arr 

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return self.mergeArrays(self.mergeSort(left), self.mergeSort(right))

    def mergeArrays(self, left, right):
        result = [None] * (len(left) + len(right))
        l = r = k = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result[k] = left[l]
                l += 1
            else:
                result[k] = right[r]
                r += 1
            k += 1

        # check if any element in left
        while l < len(left):
            result[k] = left[l]
            l += 1
            k += 1

        # check if any element in right
        while r < len(right):
            result[k] = right[r]
            r += 1
            k += 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.mergeSort([4, 2, 7, 4, 5, 6]))