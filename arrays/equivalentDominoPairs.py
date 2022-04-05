import collections


class Solution:
    def numberOfPairs(self, dominos):
        res = 0 
        c = collections.Counter()
        for a, b in dominos:
            res += c[(a, b)]
            if a != b: # avoid double count
                res += c[(b, a)]
            c[(a, b)] += 1

        return res

if __name__ == '__main__':
    dominos = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2], [1, 2]]
    s = Solution()
    print(s.numberOfPairs(dominos))