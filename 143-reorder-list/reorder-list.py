# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slowptr, fastptr = head, head.next
        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        
        #reversing the second half of LL
        rvptr = slowptr.next
        prevptr = slowptr.next = None
        while rvptr:
            temp = rvptr.next
            rvptr.next = prevptr
            prevptr = rvptr
            rvptr = temp

        #merging the two halfs
        firstptr, secondptr = head, prevptr
        while secondptr:
            tmp1, tmp2 = firstptr.next, secondptr.next
            firstptr.next = secondptr
            secondptr.next = tmp1
            firstptr, secondptr = tmp1, tmp2


        