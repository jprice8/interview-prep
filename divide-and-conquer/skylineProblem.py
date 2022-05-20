from typing import List


class Solution:
    def skyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def mergeSort(bsList):
            if len(bsList) == 0:
                return []

            if len(bsList) == 1:
                return [[bsList[0][0], bsList[0][2]], [bsList[0][1], 0]]

            mid = len(bsList) // 2
            left = mergeSort(bsList[:mid])
            right = mergeSort(bsList[mid:])
            return merge(left, right)

        def merge(left, right):
            def update(x, y, result):
                if not result or (result[-1][0] != x and result[-1][1] != y):
                    result.append([x, y])
                else:
                    result[-1][1] = y

            mergedBuildings = []
            k = l = r = 0
            currx, curry = 0, 0
            ly, ry = 0, 0
            while l < len(left) and r < len(right):
                x1, y1 = left[l]
                x2, y2 = right[r]
                if x1 < x2:
                    l += 1
                    ly = y1
                else:
                    r += 1
                    ry = y2

                currx = min(x1, x2)
                curry = max(ly, ry)
                update(currx, curry, mergedBuildings)

            # finish left
            while l < len(left):
                x1, y1 = left[l]
                l += 1
                update(x1, y1, mergedBuildings)

            # finish right
            while r < len(right):
                x1, y1 = right[r]
                r += 1
                update(x1, y1, mergedBuildings)

            return mergedBuildings

        return mergeSort(buildings)

if __name__ == '__main__':
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    s = Solution()
    print(s.skyline(buildings)) # [[2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]