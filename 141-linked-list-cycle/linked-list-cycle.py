# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowptr, fastptr = head, head

        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if slowptr == fastptr:
                return True
        
        return False

        
        