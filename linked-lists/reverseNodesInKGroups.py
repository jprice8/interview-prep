from ListNode import ListNode


class Solution:
    def reverseList(self, head, k):
        dummy = ListNode(0)
        dummy.next = head 
        groupPrev = dummy 

        # 1 -> 2 -> 3
        # 1 -> 3 -> 2
        while True:
            kthNode = self.getKth(groupPrev, k)
            if not kthNode:
                break 
            groupNext = kthNode.next 

            # reverse group
            prev, curr = kthNode.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev 
                prev = curr 
                curr = tmp

            tmp = groupPrev.next 
            groupPrev.next = kthNode
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next 
            k -= 1
        return curr

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)


    s = Solution()
    print(s.reverseList(l1, 2))