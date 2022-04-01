class Solution:
    def findSquareRoot(self, n: int) -> int:
        num_list = [num for num in range(1, n + 1)]
        left, right = 0, len(num_list) - 1
        closest_num = -1
        while left <= right:
            mid = (left + right) // 2
            curr_squared = num_list[mid] * num_list[mid]
            if curr_squared <= n:
                left = mid + 1
                closest_num = num_list[mid]
            else:
                right = mid - 1
        return closest_num


if __name__ == '__main__':
    s = Solution()
    print(s.findSquareRoot(1))