from typing import List, Optional


class ListNode:
    def __init__(self, val, nxt):
        self.val = val 
        self.next = nxt


def mergeKSortedLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    pass


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
    print(mergeKSortedLists(listOfNodes))