"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


#Solution
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self,x):
#        self.val = x
#        self.next = None

class Solution:
    def addTwoNumbers(self, li: ListNode, l2: ListNode) -> ListNode:
        p1,p2,dum,rem = l1, l2, ListNode(0),0
        p = dum
        while p1 or p2:
            cur = (p1.val if p1 else 0) + (p2.val if p2 else 0) + rem
            rem, cur = cur // 10, cur %10
            p.next = ListNode(cur)
            p,p1,p2 = p.next, p1.next if p1 else p1, p2.next if p2 else p2
        if rem: p.next = ListNode(rem)
        return dum.next