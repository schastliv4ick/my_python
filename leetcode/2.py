# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            digit = l1.val + l2.val
            carry = digit // 10
            current.next = ListNode(digit % 10)

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        
        