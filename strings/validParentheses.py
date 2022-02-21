class MySolution:
    def isValid(self, s):
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else "#"

                if top_element != bracket_map[char]:
                    return False 

            else:
                stack.append(char)

        return not stack


if __name__ == '__main__':
    s = '({'
    solution = MySolution()
    print(solution.isValid(s))