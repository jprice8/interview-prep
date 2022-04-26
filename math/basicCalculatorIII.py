class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        ops = set(['+', '-', '*', '/'])
        def helper():
            nonlocal i 
            stack = []
            num = 0
            op = '+'

            while i < len(s):
                char = s[i]
                # base case
                if char.isdigit():
                    num = (num * 10) + int(char)
                elif char == '(':
                    i += 1
                    num = helper()

                if char in ops or i == len(s) - 1 or char == ')':
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    elif op == '*':
                        stack.append(stack.pop() * num)
                    elif op == '/':
                        stack.append(stack.pop() // num)

                    num = 0
                    op = char 
                    if char == ')':
                        break

                i += 1

            res = 0
            while stack:
                res += int(stack.pop())
            return res
        return helper()


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate('(1 + 1) / 2'))