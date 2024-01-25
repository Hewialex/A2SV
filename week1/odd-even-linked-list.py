# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        oddHead = head
        oddTail = head
        evenHead = head.next
        evenTail = head.next

        curr = head.next.next
        index = 3

        while curr:
            if index % 2 == 1:
                oddTail.next = curr
                oddTail = curr
            else:
                evenTail.next = curr
                evenTail = curr

            curr = curr.next
            index += 1

        oddTail.next = evenHead
        if evenTail:
            evenTail.next = None

        return oddHead
            