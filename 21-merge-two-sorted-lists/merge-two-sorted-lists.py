# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #this checks if one of the lists has no nodes left
        if not list1 or not list2:
            #this will return the list that still has nodes left
            return list1 or list2
        
        if list1.val <= list2.val: #compares current nodes
            #pass through lists to compare next
            #list1.next is a list without the compared node [1,2,3,4] --> [2,3,4]
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

            