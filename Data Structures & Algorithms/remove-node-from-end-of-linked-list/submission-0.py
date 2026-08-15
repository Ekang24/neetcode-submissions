# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        nth = len(arr) - n
        del arr[nth]

        return self.linkedlist(arr)

    def linkedlist(self,arr):
        dummy = ListNode()
        current = dummy

        for num in arr:
            current.next = ListNode(num)
            current = current.next
        return dummy.next
        

        