# left (lru) -> (2, 2) -> (1, 1) -> right (most recent)
# { 1: Node(1), 2: Node(2) }

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None 
        self.prev = None

    def __repr__(self) -> str:
        return str(f'node({self.key})')


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def __repr__(self) -> str:
        return str(self.cache)

    # LL helpers
    # always add to far right of list
    def _addNode(self, node: Node) -> Node:
        prev_right = self.right.prev

        self.right.prev = node
        prev_right.next = node

        node.prev = prev_right
        node.next = self.right

        return node

    # find node and remove from list
    def _removeNode(self, node: Node):
        # handle error
        if not self.left.next:
            return

        head = self.left.next
        while head.key != node.key:
            head = head.next 

        head_prev = head.prev 
        head_nxt = head.next
        head.prev.next = head_nxt
        head.next.prev = head_prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._removeNode(node)
            self._addNode(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._removeNode(self.cache[key])
        self.cache[key] = Node(key, value)
        self._addNode(self.cache[key])

        # if cache at capacity, evict
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self._removeNode(lru_node)
            del self.cache[lru_node.key]


if __name__ == '__main__':
    lru = LRUCache(2)
    print(lru.put(2, 1))
    print(lru.put(1, 1))
    print(lru.put(2, 3))
    print(lru.put(4, 1))
    print(lru.get(1)) # 2
    print(lru.get(2)) # 6