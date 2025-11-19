# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        perv, curr = temp , head

        while curr:
            if curr.val == val:
                perv.next = curr.next
            else:
                perv = curr
            curr = curr.next
        
        return temp.next