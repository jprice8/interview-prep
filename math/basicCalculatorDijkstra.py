from re import S


class Solution:
    def basicCalculator(self):
        pass

    def dijkstraTwoStack(self, s: str) -> int:
        def collectNumber(i):
            res = []
            while i < len(s) and s[i].isdigit():
                res.append(s[i])
                i += 1
            return i, ''.join(res)

        def evaluate(op, val1, val2):
            if op == '+':
                return val1 + val2 
            elif op == '-':
                return val1 - val2 
            elif op == '*':
                return val1 * val2 
            elif op == '/':
                # truncate towards zero, not towards one
                return int(val1 / val2)

        def precedence(op):
            if op == '+' or op == '-':
                return 1 
            if op == '*' or op == '/':
                return 2
            return 0

        # two stacks
        ops = []
        values = []
        # while there's numbers to be seen
        i = 0
        while i < len(s):
            if s[i] == ' ':
                continue
            # 1) if char is a number
            if s[i].isdigit():
                i, num = collectNumber(i)
                values.append(int(num))
                continue

            # 2) if char is opening paren
            elif s[i] == '(':
                ops.append('(')

            # 3) if char is closing paren
            elif s[i] == ')':
                while ops[-1] != '(':
                    op = ops.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    result = evaluate(op, val1, val2)
                    values.append(result)
                # pop opening paren
                ops.pop()

            # 4) an operator
            else:
                while ops and precedence(ops[-1]) >= precedence(s[i]):
                    op = ops.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    result = evaluate(op, val1, val2)
                    values.append(result)
                # push op onto the ops stack
                ops.append(s[i])

            i += 1

        # while ops stack is not empty
        while ops:
            op = ops.pop()
            val2 = values.pop()
            val1 = values.pop()
            # apply the operator to the operands, in correct order
            result = evaluate(op, val1, val2)
            # push result back onto values stack
            values.append(result)

        return values[0]


if __name__ == '__main__':
    s = Solution()
    # print(s.dijkstraTwoStack("2*(5+5*2)/3+(6/2+8)")) #21
    print(s.dijkstraTwoStack("(0-3)/4"))