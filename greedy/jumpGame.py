class Solution:
    def jumpGame(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i 

        return True if goal == 0 else False

if __name__ == '__main__':
    s = Solution()
    print(s.jumpGame([3, 2, 1, 0, 4]))