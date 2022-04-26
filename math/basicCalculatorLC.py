class Solution:
    def calculate(self, s: str) -> int:
        def helper(s, start):
            operand = result = 0
            nextSign = 1 # 1 for pos, -1 for neg (we always add)
            i = start 
            while i < len(s) - 1:
                i += 1
                char = s[i]

                if char == ' ':
                    continue 

                if char.isnumeric():
                    # add digit to operand (could be multiple)
                    operand = 10 * operand + int(char)
                elif char == '(':
                    # new sub-expression -> recursive call
                    end, operand = helper(s, i)
                    i = end 
                elif char == ')':
                    # end sub-expression -> base case
                    break 

                else:
                    # operator
                    result += nextSign * operand
                    nextSign = 1 if char == '+' else -1
                    operand = 0

            return i, result + (nextSign * operand)
        return helper(s, -1)[1]



if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate('(4-2)+2'))
