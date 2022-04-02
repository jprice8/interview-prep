from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        # count up characters that appear in the string
        str_count = Counter(s)
        # store negative value since we want a max heap
        pq = [(-value, key) for key, value in enumerate(s)]
        # return empty string if there are too many of one character
        if - pq[0][0] > (n + 1) // 2:
            return ""
        # stores the resulting char array to be converted to string
        res = [None] * n

if __name__ == '__main__':
    s = Solution()
    print(s.reorganizeString("aab"))