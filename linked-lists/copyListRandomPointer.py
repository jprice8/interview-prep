class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next 
        self.random = random
    def __repr__(self):
        result = []
        curr = self
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return repr(result)

class Solution:
    def copyListRandom(self, head):
        oldToCopy = { None: None }

        curr = head 
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy 
            curr = curr.next 

        # second pass
        curr = head 
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next 

        return oldToCopy[head]


if __name__ == '__main__':
    head = Node(7)
    node13 = Node(13)
    head.next = node13 
    node11 = Node(11)
    node13.next = node11 
    node10 = Node(10)
    node11.next = node10
    node1 = Node(1)
    node10.next = node1

    node13.random = head
    node11.random = node1
    node10.random = node11 
    node1.random = head

    s = Solution()
    print(s.copyListRandom(head))