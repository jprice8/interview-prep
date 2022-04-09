from collections import Counter
from typing import Dict, List


class Solution:
    def findAnagrams(self, original: str, check: str) -> List[int]:
        res = []
        checkMap = Counter(check)

        # iter through original
        for idx in range((len(original) + 1) - len(check)):
            # slice sliding window
            currSlice = original[idx : idx + len(check)]
            # call helper
            if self.isAnagram(currSlice, checkMap):
                # if slice is anagram
                res.append(idx)

        return res
                
    def isAnagram(self, currSlice: str, checkMap: Dict[str, int]) -> bool:
        currMap = Counter(currSlice)
        return currMap == checkMap

    
    def slidingWindowAM(self, s, p):
        check_count = Counter(p)
        window_letter_count = {}
        match_count = 0

        def change_letter(letter, delta):
            nonlocal match_count
            if letter not in window_letter_count:
                window_letter_count[letter] = 0
            if letter in check_count and window_letter_count[letter] == check_count[letter]:
                match_count -= 1
            window_letter_count[letter] += delta
            if letter in check_count and window_letter_count[letter] == check_count[letter]:
                match_count += 1

        check_len = len(p)
        original_len = len(s)

        # the value that match_count must equal for letter count and window letter count to match
        match_threshold = len(check_count.keys())
        res = []

        if original_len < check_len:
            return res
        # init starting window
        for i in range(len(p)):
            change_letter(s[i], 1)
        if match_count == match_threshold:
            res.append(0)
        # move the sliding window and check if window is anagram
        for i in range(original_len - check_len):
            change_letter(s[i + check_len], 1)
            change_letter(s[i], -1)
            if match_count == match_threshold:
                res.append(i + 1)
        return res

    def slidingWindowLC(self, s, p):
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()

        ouput = []
        for i in range(ns):
            # add right window
            s_count[s[i]] += 1
            # remove from left
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1

            # compare array in the sliding window
            # with ref array
            if p_count == s_count:
                ouput.append(i - np + 1)

        return ouput
            

if __name__ == '__main__':
    s = Solution()
    print(s.slidingWindowLC("abab", "ab")) # [0, 1, 2]