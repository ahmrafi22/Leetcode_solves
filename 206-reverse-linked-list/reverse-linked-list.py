# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        rev_list = None
        current = head

        while current:
            next_node = current.next
            current.next = rev_list
            rev_list = current
            current = next_node
    
        return rev_list
        