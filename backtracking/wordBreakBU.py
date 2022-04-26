from tkinter import E


class Solution:
    def wordBreak(self, s, wordDict):
        result = [False for _ in range(len(s) + 1)]
        wordSet = set(wordDict)
        result[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                substring = s[j:i]
                if substring in wordSet and result[j]:
                    result[i] = True 

        return result[-1]

    def wordBreak2(self, string, words):
        if not words:
            return False 

        dp = [False] * (len(string) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                substring = s[j:i]
                if dp[j] and substring in words:
                    dp[i] = True 
                    break 
        
        return dp[-1]

    def concatenatedWords(self, words):
        res = []
        preWords = set()

        words.sort(key = len)

        for word in words:
            if self.wordBreak2(word, preWords):
                res.append(word)
            preWords.add(word)

        return res

if __name__ == '__main__':
    s = 'leetcode'
    wordDict = ['leet', 'code']
    sol = Solution()
    # print(sol.wordBreak(s, wordDict))
    words = ['cat', 'dog', 'catdog']
    print(sol.concatenatedWords(words))