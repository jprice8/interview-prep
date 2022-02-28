import collections
from typing import List


# O(nmlog(m)) time | O(nm) space - where n is the length of strs and m is the length of strs[i]
class Solution:
    def groupAnagrams(self, strs):
        result = []
        charMap = collections.defaultdict(list)

        for word in strs:
            sortedWord = sorted(word)
            sortedWord = ''.join(sortedWord)
            charMap[sortedWord].append(word)

        for _, value in charMap.items():
            result.append(value)

        return result

    def optimalSolution(self, strs):
        charMap = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26 
            for char in word:
                count[ord(char) - ord('a')] += 1
            charMap[tuple(count)].append(word)

        return charMap.values()



if __name__ == '__main__':
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    s = Solution()
    print(s.optimalSolution(strs))