class Solution:
    def longestSubstring(self, s):
        def get_length(l, r):
            return r - l + 1
        char_set = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            res = max(res, get_length(left, right))

        return res

            



if __name__ == '__main__':
    string = 'abcdbea'
    s = Solution()
    print(s.longestSubstring(string))