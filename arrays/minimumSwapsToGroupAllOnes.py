from typing import List


class Solution:
    def minimumSwapsToGroupAllOnes(self, data: List[int]) -> int:
        count_ones = sum(data)
        max_ones, current_ones = 0, 0
        left, right = 0, 0
        while right < len(data):
            current_ones += data[right]
            right += 1

            if right - left > count_ones:
                current_ones -= data[left]
                left += 1

            max_ones = max(max_ones, current_ones)

        return count_ones - max_ones 


if __name__ == '__main__':
    data = [1, 0, 1, 0, 1]
    data1 = [1,0,1,0,1,0,0,1,1,0,1]
    s = Solution()
    print(s.minimumSwapsToGroupAllOnes(data))