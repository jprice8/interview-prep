from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        count_ones = sum(data)
        max_ones, curr_ones = 0, 0 
        l, r = 0, 0
        while r < len(data):
            curr_ones += data[r]
            r += 1

            if r - l > count_ones:
                curr_ones -= data[l]
                l += 1

            max_ones = max(max_ones, curr_ones)

        return count_ones - max_ones

if __name__ == '__main__':
    s = Solution()
    print(s.minSwaps([1, 0, 0, 1, 1, 1]))
    # print(s.minSwaps([1]))