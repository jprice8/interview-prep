from typing import List


class Solution:
    def vanilla(self, arr: List[int], target: int) -> int:
        # Perform binary search
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            # left
            if target < arr[m]:
                r = m - 1
            # right
            elif target > arr[m]:
                l = m + 1
            # match
            else:
                return m

        # no match
        return -1


if __name__ == '__main__':
    arr = [1, 3, 6, 8, 9, 10]
    target = 11 
    s = Solution()
    print(s.vanilla(arr, target))