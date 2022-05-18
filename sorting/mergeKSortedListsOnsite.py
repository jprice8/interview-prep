class Content:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __repr__(self) -> str:
        return f'Content {self.value}'


class Solution:
    def mergeKSorted(self, lists):
        if len(lists) < 2:
            return lists

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeSorted(l1, l2))
            lists = mergedLists

        return [content.value for content in lists[0]]


    def mergeSorted(self, left, right):
        if not left:
            return right
        if not right:
            return left

        result = [None] * (len(left) + len(right))
        l = r = k = 0
        while l < len(left) and r < len(right):
            if left[l].value <= right[r].value:
                result[k] = left[l]
                l += 1
            else:
                result[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            result[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            result[k] = right[r]
            r += 1
            k += 1

        return result


if __name__ == '__main__':
    l1 = [Content(1, 1), Content(4, 4), Content(7, 7)]
    l2 = [Content(2, 2), Content(5, 5), Content(8, 8)]
    l3 = [Content(3, 3), Content(6, 6), Content(9, 9)]

    s = Solution()
    print(s.mergeKSorted([l1, l2, l3]))