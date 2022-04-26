class Solution:
    # 1) Need two stacks: numbers, operators.
    # 2) Need func to parse the text and populate stacks.
    # 3) Evaluate expression by popping from stacks.

    # '1 + 1' Done
    # '2-1 + 2' -> 2-3 -> -1
    # '(4-2)+1'
    # '2*1-2' -> 2-2 -> 0
    #  2* -1 -> -2
    def calculate(self, s: str) -> int:
        # 1) stacks
        nums = [] # [2, 1, 2]
        ops = [] # [-, +]

        # 2) parse
        i = 0
        while i < len(s):
            char = s[i]

            # if starting parentheses
            if char == '(':
                startIdx = i + 1
                # complete inside parentheses
                while i < len(s) and s[i] != ')':
                    i += 1
                endIdx = i 
                recursiveResult = self.calculate(s[startIdx:endIdx])
                nums.append(recursiveResult)

            # if num
            elif char.isnumeric():
                nums.append(int(char))
            elif char == ' ':
                continue
            # if op
            else:
                ops.append(char)

            i += 1

        # 3) Eval
        res = 0 # 3
        while ops:
            num2 = nums.pop() # 3
            num1 = nums.pop() # 2
            op = ops.pop() # -

            res = self.evaluate(num1, num2, op)

            nums.append(res)

        return nums[0]

    def evaluate(self, num1, num2, op):
        if op == '+':
            return num1 + num2 # 3
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 // num2



if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate('(4-2)+1'))