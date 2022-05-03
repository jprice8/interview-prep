class Solution:
    def concatWords(self, words):
        word_set = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in word_set and (suffix in word_set or dfs(suffix)):
                    memo[word] = True
                    break
            return memo[word]
                    
        return [word for word in words if dfs(word)]

if __name__ == '__main__':
    s = Solution()
    print(s.concatWords(['cat', 'dog', 'catdog']))