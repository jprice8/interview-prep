class Solution:
    # O(n) time | O(1) space - where n is the lenght of string.
    def characterReplacement(self, s, k):
        count = {}
        res = 0

        left = 0
        maxLength = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0) 
            maxLength = max(maxLength, count[s[right]])

            if (right - left + 1) - maxLength > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res

if __name__ == '__main__':
    string = 'AABABBA'
    k = 1
    s = Solution()
    print(s.characterReplacement(string, k))