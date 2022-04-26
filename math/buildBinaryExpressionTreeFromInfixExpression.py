import collections


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right


class Solution:
    # Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]
    def expTree(self, s: str) -> 'Node':
        tokens = collections.deque(list(s))
        return self.parse_expression(tokens)
    
    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while len(tokens) > 0 and tokens[0] in ['+', '-']:
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs
    
    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while len(tokens) > 0 and tokens[0] in ['*', '/']:
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs
    
    def parse_factor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft()
            node = self.parse_expression(tokens)
            tokens.popleft()
            return node
        else:
            token = tokens.popleft()
            return Node(val=token)


class TwoStackSolution:
    def expTree(self, s: str) -> 'Node':
        operandStack = []
        operatorStack = []
        # CONSIDERATION: HIGHER THE OPERATION HIGHER IS THE PRECEDENCE
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
        prevScore = 0
        
        def buildSubTree():
            right = operandStack.pop()
            left = operandStack.pop()
            operandStack.append(Node(operatorStack.pop(), left, right))
        
        for ch in s:
            if ch == ')':
                while operatorStack[-1] != '(':
                    buildSubTree()
                
                # POP OUT '('
                operatorStack.pop()
                prevScore = precedence[operatorStack[-1]] if operatorStack else 0
                    
            elif ch in precedence:
                if ch == '(':
                    prevScore = 0
                    
                elif prevScore < precedence[ch]:
                    prevScore = precedence[ch]
                    
                else:
                    while operatorStack and operatorStack[-1] != '(' and prevScore >= precedence[ch]:
                        buildSubTree()
                        
                        if operatorStack:
                            prevScore = precedence[operatorStack[-1]]
                    
                    prevScore = precedence[ch]
                operatorStack.append(ch)
                
            else:
                operandStack.append(Node(ch))
        
        while operatorStack and operatorStack[-1] != '(':
            buildSubTree()
        
        return operandStack[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.expTree('3*4-2*5'))