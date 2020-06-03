# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node.next
        node.val = temp.val
        node.next = temp.next

# Fast solution is to copy the data from the next node 
# to the node to be deleted and delete the next node.