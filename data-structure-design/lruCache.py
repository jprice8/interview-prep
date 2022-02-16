# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None


# class LRUCache:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = {} # map key to node

#         self.left, self.right = Node(0, 0), Node(0, 0)
#         self.left.next, self.right.prev = self.right, self.left

#     # Remove node from list
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev

#     # Insert node at right
#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node 
#         node.next, node.prev = nxt, prev

#     def get(self, key):
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key, value):
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.capacity:
#             # Remove from the list and delete the LRU from hashmap
#             lru = self.left.next 
#             self.remove(lru)
#             print(lru in self.cache)
#             del self.cache[lru.key]


class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = None 
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right 
        self.right.prev = self.left

    def _insert(self, node):
        rightPrev, rightNext = self.right.prev, self.right
        rightPrev.next = rightNext.prev = node 
        node.next, node.prev = rightNext, rightPrev

    def _remove(self, key):
        prevNode, nextNode = self.cache[key].prev, self.cache[key].next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key):
        """
        Take in a key and return the value of the key if key exists,
        otherwise return -1.
        """
        if key in self.cache:
            # Updating cache, if hit
            # Remove from list
            self._remove(key)
            # Insert at right of list
            self._insert(self.cache[key])

            return self.cache[key].value
        # Return if cache miss
        return -1

    def put(self, key, value):
        """
        Update the value of the key, if key exists. Otherwise, add the
        key-value pair to the cache.

        If the number of keys exceeds the capacity, evict the LRU key.
        """
        pass


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1) # cache is {1: 1}
    cache.put(2, 2) # cache is {1: 1, 2: 2}
    cache.get(1) # return 1
    cache.put(3, 3) # cache is {1: 1, 3: 3}
    cache.get(2) # return -1, not found
    cache.put(4, 4) # cache is {4: 4, 3: 3}
    cache.get(1) # return -1, not found
    cache.get(3) # return 3
    cache.get(4) # return 4