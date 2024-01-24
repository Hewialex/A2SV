# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = ListNode(-200)
        cur = rev
        while head:
            if cur.val == head.val:
                head = head.next
            else:
                cur.next = head
                cur = cur.next
                head = head.next
        cur.next = None
        return rev.next

        