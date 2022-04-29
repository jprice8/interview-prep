import collections


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.freq = 1


class DLinkedList:
    def __init__(self):
        self.left = Node(None, None)
        self.right = Node(None, None)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node):
        # always insert at far right
        prev_node = self.right.prev
        self.right.prev = node 
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right

    def remove(self, node: Node):
        prev_node = node.prev
        nxt_node = node.next
        node.prev.next = nxt_node
        node.next.prev = prev_node


class LFUCache:
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0
        self._cache = {}

    def _update(self, node: Node):
        # 1) remove node from curr freq DLL
        freq = node.freq
        self._freq[freq].remove(node)

        # 2) if we just removed the only node in the minfreq DLL, minfreq moves up.
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1

        # 3) insert into new freq DLL
        node.freq += 1
        self._freq[node.freq].insert(node)


    def get(self, key: int) -> int:
        if key in self._cache:
            node = self._cache[key]
            self._update(node)
            return self._cache[key].value
        return -1

    def put(self, key: int, value: int):
        if key in self._cache:
            node = self._cache[key]
            self._update(node)
            node.value = value

        else:
            if self._size == self._capacity:
                lru_node = self._freq[self._minfreq].left.next
                self._freq[self._minfreq].remove(lru_node)
                del self._cache[lru_node.key]
                self._size -= 1

            node = Node(key, value)
            self._cache[key] = node 
            self._freq[1].insert(node)
            self._minfreq = 1
            self._size += 1


if __name__ == '__main__':
    lfu = LFUCache(2)
    print(lfu.put(1, 1))
    print(lfu.put(2, 2))
    print(lfu.get(1))
    print(lfu.put(3, 3))
    print(lfu.get(2))  # -1
