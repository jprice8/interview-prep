class ListNode:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next, self.prev = None, None
    def __repr__(self) -> str:
        return str(self.val)

class LruCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # linked list
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    def __repr__(self) -> str:
        return str(self.cache)

    # remove from list
    def _remove(self, node):
        currNode = self.left
        while currNode.key != node.key:
            currNode = currNode.next 

        prevNode = currNode.prev
        currNode.prev = currNode.next 
        currNode.next = prevNode

    # insert at right
    def _insert(self, node):
        prevRight = self.right.prev
        self.right.prev.next = node 
        node.prev = prevRight

        node.next = self.right
        self.right.prev = node

    # O(1) time
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if key exists.
        Otherwise, add the KV pair to the cache.
        If the number of keys exceeds the capacity from
        this operation, evict the LRU key.
        """
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self._insert(self.cache[key])

        # check exceeding capacity
        if len(self.cache) > self.capacity:
            self._remove(self.left.next)


if __name__ == '__main__':
    lruCache = LruCache(2)
    print(lruCache.put(1, 1))
    print(lruCache.put(2, 2))
    print(lruCache.get(1))
    print(lruCache.put(3, 3)) # Evict 2, cach is now {1:1, 3:3}
    print(lruCache.get(2)) # -1
    print(lruCache.put(4, 4))
    print(lruCache.get(1)) # -1