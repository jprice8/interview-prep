from linkedList import LinkedList

# O(m + n) time
# O(1) space
def mergeTwoSortedLists(list1, list2):
    prehead = LinkedList(-1)
    prev = prehead

    p1 = list1
    p2 = list2 

    while p1 is not None and p2 is not None:
        if p1.value <= p2.value:
            prev.next = p1 
            p1 = p1.next 
        else:
            prev.next = p2 
            p2 = p2.next 

        prev = prev.next 

    prev.next = p1 if p1 is not None else p2 

    return prehead.next

# O(m + n) time
# O(m + n) space
def recursiveSolution(list1, list2):
    if list1 is None:
        return list2 
    if list2 is None:
        return list1 

    if list1.value < list2.value:
        list1.next = recursiveSolution(list1.next, list2)
        return list1 
    else:
        list2.next = recursiveSolution(list1, list2.next)
        return list2
    

if __name__ == '__main__':
    node1a = LinkedList(1)
    node1b = LinkedList(1)
    node2 = LinkedList(2)
    node3 = LinkedList(3)
    node4a = LinkedList(4)
    node4b = LinkedList(4)

    node1a.next = node2
    node2.next = node4a

    node1b.next = node3
    node3.next = node4b

    # print(mergeTwoSortedLists(node1a, node1b)) # [1, 1, 2, 3, 4, 4]
    print(recursiveSolution(node1a, node1b))