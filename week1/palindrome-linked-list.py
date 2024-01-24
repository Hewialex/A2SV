# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = ListNode
        cur = deepcopy(head)
        while head:
            temp = head.next
            head.next = rev
            rev = head
            head = temp
        while cur:
            if cur.val != rev.val:
                return False
            cur = cur.next
            rev = rev.next
        return True
        