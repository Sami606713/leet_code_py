# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        -Inisalize three variable
        1-variable that store the original list
        2-store None
        3-Store None

        -Itrate the original list and swap the values in list
        after the end of the loop re-assign the head
        """
        curr=head
        next=None
        prev=None

        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        head=prev
        return head


        