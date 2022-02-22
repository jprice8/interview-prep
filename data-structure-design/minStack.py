import collections


class MinStackLeetcode:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        # Always put the number onto the main stack
        self.stack.append(val)
        # If the in stack is empty, or this number is smaller than the top
        # of the min stack, put it on with a count of 1.
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])

        # Else if this number is equal to what is currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self):
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1][0]

    def printStack(self):
        return self.stack


if __name__ == '__main__':
    minStack = MinStackLeetcode()

    minStack.push(-2)
    print(minStack.printStack())
    minStack.push(0)
    print(minStack.printStack())
    minStack.push(-3)
    print(minStack.printStack())
    print(minStack.getMin())
    print(minStack.printStack())
    print(minStack.pop())
    print(minStack.printStack())
    print(minStack.top())
    print(minStack.getMin())