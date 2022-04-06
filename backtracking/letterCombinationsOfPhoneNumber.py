from typing import List


class Solution:
    def letterCombos(self, digits: str) -> List[str]:
        key_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        def dfs(path, res):
            nonlocal key_map
            # base
            if len(path) == len(digits):
                res.append(''.join(path))
                return 

            # children
            next_number = digits[len(path)]
            for char in key_map[next_number]:
                path.append(char)
                dfs(path, res)
                path.pop()

        res = []
        dfs([], res)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombos("23"))