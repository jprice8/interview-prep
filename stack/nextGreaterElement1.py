from typing import List


class Solution:
    # O(n * m) time | O(n) space
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            number1 = nums1[i]
            
            l = 0
            while l < len(nums2) and nums2[l] != number1:
                l += 1
                
            r = l + 1
            while r < len(nums2) and nums2[l] >= nums2[r]:
                r += 1
                
            # handle index error
            if r < len(nums2) and nums2[l] < nums2[r]:
                ans.append(nums2[r])
            else:
                ans.append(-1)
                
        return ans

    # O(n) time | O(n) space - where n is the length of nums2
    def nextGreaterElementStack(self, nums1, nums2):
        stack = [nums2[0]]
        numberMap = {}
        for idx in range(1, len(nums2)):
            num2 = nums2[idx]
            # while num2 is greater than stack[top], pop stack and add to map
            while len(stack) and num2 > stack[-1]:
                stackTop = stack.pop()
                numberMap[stackTop] = num2 
            stack.append(num2)

        # Handle remaining nums in stack
        while len(stack):
            stackNum = stack.pop()
            numberMap[stackNum] = -1

        ans = []
        for num in nums1:
            ans.append(numberMap[num])

        return ans

    def nextGreaterElementStackPythonic(self, nums1, nums2):
        nums1Idx = { val: idx for idx, val in enumerate(nums1) }
        ans = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                stackTop = stack.pop()
                idx = nums1Idx[stackTop]
                ans[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return ans


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    s = Solution()
    # print(s.nextGreaterElement(nums1, nums2))
    print(s.nextGreaterElementStack(nums1, nums2))