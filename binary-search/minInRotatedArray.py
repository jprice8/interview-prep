class Solution:
    def findMin(self, arr):
        boundary_idx = -1
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= arr[-1]:
                # False
                r = mid - 1
                boundary_idx = mid 
            else:
                # True
                l = mid + 1

        return boundary_idx


if __name__ == '__main__':
    arr = [3, 4, 5, 1, 2]

    s = Solution()
    print(s.findMin(arr))