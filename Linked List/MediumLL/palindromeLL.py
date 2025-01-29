'''Given the head of a singly linked list, return true if it is a palindrome or false otherwise.'''


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def checkPalindrome(slow, lst):
    for i in range(len(lst)-1, -1, -1) :
        if slow.val != lst[i] :
            return 0
        slow = slow.next
    return 1

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None :
            return True
        
        fast = slow = head
        lst = []
        while fast and fast.next:
            lst.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast == None :
            ans = checkPalindrome(slow, lst)
        else :
            if slow.next == None :
                return 0
            slow = slow.next
            ans = checkPalindrome(slow, lst)
        
        return ans