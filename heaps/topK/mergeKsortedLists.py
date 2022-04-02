import heapq
from typing import List, Optional
from queue import PriorityQueue


class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None

    def __repr__(self) -> str:
        return str(self.val)


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
        heap = []
        res = []
        for current_list in lists:
            # push first number of each list into the heap
            heapq.heappush(heap, (current_list[0], current_list, 0)) # 1

        while heap:
            val, current_list, head_idx = heapq.heappop(heap)
            res.append(val)
            head_idx += 1
            if head_idx < len(current_list):
                heapq.heappush(heap, (current_list[head_idx], current_list, head_idx))

        return res

    def mergeLinkedListHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel = curr = ListNode(0)
        heap = []

        for idx, val in enumerate(lists):
            node = lists[idx]
            heapq.heappush(heap, (node.val, idx))

        while heap:
            val, head_idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            node = lists[head_idx]
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, head_idx))
        
        return sentinel

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head.next

if __name__ == '__main__':
    lists = [
        [1, 2, 5],
        [3, 6, 8],
        [4, 7, 9],
    ]

    node1 = ListNode(1)
    node1.next = ListNode(4)
    node1.next.next = ListNode(5)

    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)

    node3 = ListNode(2)
    node3.next= ListNode(6)

    llists = [node1, node2, node3]
    s = Solution()
    print(s.mergeKLists(llists))