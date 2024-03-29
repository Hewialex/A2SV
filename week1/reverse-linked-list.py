# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        rev = None
        while head:
            temp = head.next
            head.next = rev
            rev = head
            head = temp
        return rev

        