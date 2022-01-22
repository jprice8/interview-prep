def reverseString(string):
    return recursiveHelper(0, len(string) - 1, string)


def recursiveHelper(start, end, string):
    # Base case
    if start > end:
        return string
    # Swap first and last element
    string[start], string[end] = string[end], string[start]

    return recursiveHelper(start + 1, end - 1, string)


#### LeetCode Solution ####
class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        def helper(start, end, ls):
            if start >= end:
                return 

            # Swap the first and last 
            ls[start], ls[end] = ls[end], ls[start]

            return helper(start + 1, end - 1, ls)

        helper(0, len(string) - 1, string)


if __name__ == '__main__':
    string = ['h', 'e', 'l', 'l', 'o']
    # print(reverseString(string))

    leetCodeSolution = Solution()
    print(leetCodeSolution.reverseString(string))
