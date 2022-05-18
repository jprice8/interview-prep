class Content:
    def __init__(self, index, value):
        self.index = index
        self.value = value


class Solution:
    def mergeKSorted(self, lists):
        if len(lists) < 2:
            return lists

        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]
        return self.mergeSorted(left, right)

    def mergeSorted(self, left, right):
        mergedLists = [None] * (len(left) + len(right))
        l = r = k = 0
        while l < len(left) and r < len(right):
            if left[l].value <= right[r].value:
                mergedLists[k] = left[l]
                l += 1
            else:
                mergedLists[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            mergedLists[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            mergedLists[k] = right[r]
            r += 1
            k += 1

        return mergedLists


if __name__ == '__main__':
    l1 = [Content(1, 1), Content(4, 4), Content(7, 7)]
    l2 = [Content(2, 2), Content(5, 5), Content(8, 8)]
    l3 = [Content(3, 3), Content(6, 6), Content(9, 9)]

    s = Solution()
    print(s.mergeKSorted([l1, l2, l3]))