import collections


class Solution:
    def minWindow(self, s, t):
        res = ""
        smallest = float('inf')
        t_map = collections.defaultdict(int)
        for char in t:
            t_map[char] += 1

        s_map = collections.defaultdict(int)
        left = 0
        for right in range(len(s)):
            if s[right] in t_map:
                s_map[s[right]] += 1

            if s_map == t_map:
                if right - left + 1 < smallest:
                    smallest = right - left + 1
                    res = s[left:right + 1]

                    right += 1
                    left = right 

                s_map = collections.defaultdict(int)

        return res 

    def neetcode(self, s, t):
        if t == "": return ""

        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        left = 0
        for right in s:
            currChar = s[right]
            window[currChar] = 1 + window.get(currChar, 0)

            if currChar in countT and window[currChar] == countT[currChar]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)
                # pop from left of window to minimize
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        l, r = res 
        return s[l:r+1] if resLen != float('inf') else ""



if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    # print(solution.minWindow(s, t))
    print(solution.neetcode(s, t))


