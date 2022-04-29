from collections import Counter


class Solution:
    def wonderful(self, word: str) -> int:
        count = Counter()
        seen = Counter()
        seen[0] = 1

        mask = 0
        ans = 0
        for _, char in enumerate(word):
            count[char] += 1
            bit = ord(char) - ord('a')

            if count[char]&1:
                mask = mask | (1 << bit)
            else:
                mask = mask ^ (1 << bit)

            ans += seen[mask]

            for j in range(11):
                if ((1 << j) ^ mask) in seen:
                    ans += seen[(1 << j) ^ mask]

            seen[mask] += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.wonderful('aba'))