class MaxStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        newMin = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(newMin)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

if __name__ == '__main__':
    maxStack = MaxStack()
    maxStack.push(4)
    maxStack.push(3)
    maxStack.push(7)
    print(maxStack.pop())
    print(maxStack.top())
    print(maxStack.peekMax())
    print(maxStack.popMax())