import collections


class Node:
    def __init__(self, key: int, value: int):
        self.key = key 
        self.value = value 
        self.freq = 1 
        self.prev = None 
        self.next = None 

    def __repr__(self) -> str:
        return f'node({self.key})'


class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0 
    
    def __len__(self):
        return self._size

    def __repr__(self):
        result = []
        curr = self
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        return repr(result)
        
    def append(self, node: Node) -> None:
        node.next = self._sentinel.next 
        node.prev = self._sentinel
        node.next.prev = node 
        self._sentinel.next = node 
        self._size += 1

    def pop(self, node: Node = None) -> Node:
        if self._size == 0:
            return 

        if not node:
            node = self._sentinel.prev 

        node.prev.next = node.next 
        node.next.prev = node.prev 
        self._size -= 1

        return node


class LFUCache:
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity

        self._cache = {} # key: Node
        self._freq = collections.defaultdict(DLinkedList)
        self._minFreq = 0

    def __repr__(self) -> str:
        return str(self._cache)

    def _update(self, node: Node):
        freq = node.freq

        self._freq[freq].pop(node)
        if self._minFreq == freq and not self._freq[freq]:
            self._minFreq += 1

        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self, key: int) -> int:
        if key in self._cache:
            node = self._cache[key]
            self._update(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        # update key/node frequency
        if key in self._cache:
            node = self._cache[key]
            self._update(node)
            node.value = value
        else:
        # we know this is the first time seeing key
            if self._size == self._capacity:
                node = self._freq[self._minFreq].pop()
                del self._cache[node.key]
                self._size -= 1
            
            node = Node(key, value)
            self._cache[key] = node 
            self._freq[1].append(node)
            self._minFreq = 1
            self._size += 1


if __name__ == '__main__':
    lfu = LFUCache(2)
    print(lfu.put(1,1))
    print(lfu.put(2,2))
    print(lfu.get(1)) # 1
    print(lfu.put(3,3))
    print(lfu.get(2)) # -1