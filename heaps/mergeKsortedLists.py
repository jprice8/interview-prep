from typing import List, Optional
from queue import PriorityQueue


class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None


class Solution:
    # Linked list with PQ
    def mergeListsPQ(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sentinel
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next 
            node = node.next 
            if node:
                q.put((node.val, node))
        return head.next

    # List of lists with heap
    def mergeListHeap(self, lists: List[List[int]]) -> List[int]:
        pass


if __name__ == '__main__':
    lists = [
        [1, 2, 5],
        [3, 6, 8],
        [4, 7, 9],
    ]
    s = Solution()
    print(s.mergeListsPQ(lists))