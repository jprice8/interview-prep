class Solution:
    # BOTTOM UP
    def bottomUp(self, s: str, p: str) -> bool:
        pass

    # TOP DOWN MEMO
    def topDown(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            # base cases
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                # we've matched the string to the pattern
                return True
            if j >= len(p):
                # we can't match a string with a larger pattern
                return False

            # establish a match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            # is the next pattern a star?
            if (j + 1) < len(p) and p[j + 1] == '*':
                # 1) use #           2) don't use *
                
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]

            # if no star, check simple match
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)


if __name__ == '__main__':
    s = 'abc'
    p = 'a..' # true
    # p = 'a*' # true
    # p = '.b' # false
    sol = Solution()
    print(sol.topDown(s, p))