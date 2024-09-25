# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftptr = dummy
        rightptr = head

        while n > 0:
            rightptr = rightptr.next
            n -= 1
        
        while rightptr:
            leftptr = leftptr.next
            rightptr = rightptr.next
        
        leftptr.next = leftptr.next.next
        return dummy.next