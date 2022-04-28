class Solution:
    def evaluate(self, string: str) -> int:
        # '3+1'
        opStack = [] # [+, *] 
        numStack = [] # ['10, 2, 6]
        # build stacks
        i = 0
        while i < len(string):
            # char is a space
            if string[i] == ' ':
                i += 1
                continue

            elif string[i] == '(':
                opStack.append(string[i])

            # char is a number
            elif string[i].isnumeric():
                # num
                numString = []
                while i < len(string) and string[i].isnumeric():
                    numString.append(string[i])
                    i += 1
                newNum = int(''.join(numString))
                numStack.append(newNum)
                i -= 1

            # closing bracket
            elif string[i] == ')':
                while len(opStack) != 0 and opStack[-1] != '(':
                    val2 = numStack.pop()
                    val1 = numStack.pop()
                    op = opStack.pop()

                    numStack.append(self.applyOp(val1, val2, op))

            # char is an operator 
            else:
                # while top of ops has the same or 
                # greater precedence to current token,
                # which is an op. Appply op on top of ops
                # to top two elements in values stack.
                while (len(opStack) != 0 and 
                    self.precedence(opStack[-1]) >= 
                    self.precedence(string[i])):

                    val2 = numStack.pop()
                    val1 = numStack.pop()
                    op = opStack.pop()

                    numStack.append(self.applyOP(val1, val2, op))

                opStack.append(string[i])

            i += 1

        while len(opStack) != 0:
            val2 = numStack.pop()
            val1 = numStack.pop()
            op = opStack.pop()

            numStack.append(self.applyOP(val1, val2, op))

        return numStack[-1]

    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def applyOP(self, val1, val2, op):
        if op == '+':
            return val1 + val2
        elif op == '-':
            return val1 - val2
        elif op == '*':
            return val1 * val2 
        elif op == '/':
            return val1 // val2


if __name__ == '__main__':
    s = Solution()
    # print(s.evaluate('3+1'))
    print(s.evaluate('10 + 2 * 6')) # 22