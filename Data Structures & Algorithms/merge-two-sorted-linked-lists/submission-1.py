# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
                list2: Optional[ListNode]) -> Optional[ListNode]:
        
        tmpHead = ListNode()
        newCur = tmpHead

        cur1 = list1
        cur2 = list2 

        while cur1 or cur2: 

            if cur1 and cur2: 

                if cur1.val < cur2.val: 
                    newCur.next = cur1
                    newCur = cur1
                    cur1 = cur1.next
                else: 
                    newCur.next = cur2
                    newCur = cur2
                    cur2 = cur2.next

            elif cur1: 
                newCur.next = cur1
                return tmpHead.next
            elif cur2: 
                newCur.next = cur2
                return tmpHead.next

        return tmpHead.next





            

