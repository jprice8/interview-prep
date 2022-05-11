import collections


class FreqStack:

    def __init__(self):
        self.counter = {}
        self.freqGroup = collections.defaultdict(list)
        self.maxFreq = 0 # 2

    def push(self, x):
        self.counter[x] = self.counter.get(x, 0) + 1
        freq = self.counter[x] # 1
        if freq > self.maxFreq:
            self.maxFreq = freq
        self.freqGroup[freq].append(x)

    def pop(self):
        poppedVal = self.freqGroup[self.maxFreq].pop()
        self.counter[poppedVal] -= 1
        if not self.maxFreq in self.freqGroup:
            self.maxFreq -= 1
        return poppedVal

if __name__ == '__main__':
    fs = FreqStack()
    print(fs.push(5))
    print(fs.push(7))
    print(fs.push(5))
    print(fs.push(7))
    print(fs.push(4))
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())
    print(fs.pop())