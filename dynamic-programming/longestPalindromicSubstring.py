class MySolution:
    def longestPalindrome(self, string):
        return self.findPalindrome(string, "")

    def findPalindrome(self, string, longest):
        if len(string) == 0:
            return False 
        if string.lower() == string[::-1].lower():
            return True 

        for i in range(len(string)):
            prefix = string[:-1]
            isPalindrome = self.findPalindrome(prefix, longest)
            if isPalindrome:
                longest = prefix 
                return

        return longest


class BottomUp:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        # Every string with one char is a palindrome
        for i in range(len(s)):
            dp[i][i] = True 
        ans = s[0]
        for j in range(len(s)):
            for i in range(len(j)):
                if s[i] == s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j] = True 
                    if j - 1 + 1 > len(ans):
                        ans = s[i : j + 1]
        return ans

# O(n^2) time | O(1) space
class Neetcode:
    def longestPalindrome(self, string):
        res = ""
        resLen = 0

        for i in range(len(string)):
            l, r = i, i 
            while l >= 0 and r < len(string) and string[l] == string[r]:
                # Is current string length new max?
                if (r - l + 1) > resLen:
                    res = string[l:r+1]
                    resLen = r - l + 1 

                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(string) and string[l] == string[r]:
                if (r - l + 1) > resLen:
                    res = string[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

if __name__ == '__main__':
    string = 'babad'
    mySolution = MySolution()
    # print(mySolution.longestPalindrome(string)) # bab or aba

    string2 = 'cbbd'
    neetCode = Neetcode()
    # print(neetCode.longestPalindrome(string2))
    bottomUp = BottomUp()
    print(bottomUp.longestPalindrome(string2))
