from typing import List, Optional


class ListNode:
    def __init__(self, val):
        self.val = val 
        self.next = None

    def __repr__(self):
        result = []
        curr = self
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return repr(result)

    def printNodes(self):
        node = self 
        while node is not None:
            print(node.val)
            node = node.next

# O(nlogn) time | O(n) space - where n is the total number of nodes.
def mergeKSortedListsBruteForce(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    nodes = []
    head = point = ListNode(0)
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next 

    for x in sorted(nodes):
        point.next = ListNode(x)
        point = point.next 
    return head.next

# O(n * log(k)) time | O(n) space - where n is the total number of nodes and 
# k is the length of lists.
class Solution:
    def mergeKSortedListsDivideAndConquer(self, lists):
        if not lists or len(lists) == 0:
            return None 

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None 
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode(0)
        prev = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next 
            else:
                prev.next = l2 
                l2 = l2.next
            prev = prev.next

        if l1:
            prev.next = l1 
        if l2:
            prev.next = l2

        return dummy.next


class Leetcode:
    def mergeKLists(self, lists):
        numberOfLists = len(lists)
        interval = 1
        while interval < numberOfLists:
            for i in range(0, numberOfLists - interval, interval * 2):
                lists[i] = self.mergeList(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if numberOfLists > 0 else None 

    def mergeList(self, l1, l2):
        dummy = ListNode(0)
        prev = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next 
            else:
                prev.next = l2 
                l2 = l2.next
            prev = prev.next

        if l1:
            prev.next = l1 
        if l2:
            prev.next = l2

        return dummy.next


if __name__ == '__main__':
    node1a = ListNode(1)
    node1b = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4a = ListNode(4)
    node4b = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1a.next = node4a 
    node4a.next = node5

    node1b.next = node3 
    node3.next = node4b 

    node2.next = node6

    listOfNodes = [node1a, node1b, node2]
    solution = Solution()
    print(solution.mergeKSortedListsDivideAndConquer(listOfNodes))

    lc = Leetcode()
    print(lc.mergeKLists(listOfNodes))