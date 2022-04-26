from typing import List


class Solution:
    # O(c) time | O(c) space - where c is all characters in words list
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # edge case where prefix is same for both words
            # and len(w1) > len(w2)
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                # we know char in w1 comes before w2
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # perform dfs
        visit = {}  # False = visited, True = visited and in current path
        res = []  # chars to be joined at end

        def dfs(c):
            # base case
            if c in visit:
                return visit[c]

            visit[c] = True
            # recursive calls to neighbors
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True
            visit[c] = False
            # postorder visit
            res.append(c)

        for c in adj:
            if dfs(c):
                return ''
        res.reverse()
        return ''.join(res)


if __name__ == '__main__':
    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    s = Solution()
    print(s.alienOrder(words))
