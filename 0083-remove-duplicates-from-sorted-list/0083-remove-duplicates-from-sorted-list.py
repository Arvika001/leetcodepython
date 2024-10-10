# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # If the current node's value is equal to the next node's value
        if head.val == head.next.val:
            # Skip the next node and recursively call for the rest of the list
            return self.deleteDuplicates(head.next)
        else:
            # Otherwise, keep the current node and link it to the result of the recursive call
            head.next = self.deleteDuplicates(head.next)
            return head