from typing import List


class Solution:
    def permuations(self, letters: str) -> List[str]:
        def dfs(path, used, res):
            if len(path) == len(letters):
                res.append(''.join(path))
                return 

            for idx, char in enumerate(letters):
                if used[idx]:
                    continue

                # make move
                path.append(char)
                used[idx] = True
                dfs(path, used, res)
                path.pop()
                used[idx] = False

        res = []
        dfs([], [False] * len(letters), res)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permuations("abc"))