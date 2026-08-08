# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        prev = None
        slow = fast = head

        # Find middle and reverse first half
        while fast and fast.next:
            fast = fast.next.next

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # If odd number of nodes, skip middle
        if fast:
            slow = slow.next

        # Compare reversed first half with second half
        while prev and slow:
            if prev.val != slow.val:
                return False

            prev = prev.next
            slow = slow.next

        return True