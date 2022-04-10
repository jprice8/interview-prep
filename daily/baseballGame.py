from typing import List


class Solution:
    def baseball(self, ops: List[str]) -> int:
        record = []
    
        for op in ops:
            # four cases
            # 1) int -> append
            if op.isdigit() or op[0] == '-':
                record.append(int(op))
                
            # 2) C -> invalidate
            elif op == 'C':
                record.pop()
                
            # 3) D -> double and append
            elif op == 'D':
                numToAdd = record[-1] * 2
                record.append(numToAdd)
                
            # 4) + -> add last two and append
            elif op == '+':
                numToAdd = record[-1] + record[-2]
                record.append(numToAdd)
                
        return sum(record)

if __name__ == '__main__':
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    s = Solution()
    print(s.baseball(ops))