#Linked-List

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)
+ [Reorder List](#reorder-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)
## Reverse Linked List 

https://leetcode.com/problems/reverse-linked-list/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        theFirst = head
        if not theFirst or not theFirst.next:
            return theFirst
        theFirst.next, now, before = None, theFirst.next, theFirst
        while (now.next != None):
            now.next, now, before = before, now.next, now
        now.next = before
        return now

```
## Middle of the Linked List 

https://leetcode.com/problems/middle-of-the-linked-list/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        current = head
        while (current != None):
            current = current.next
            count = count + 1
        middleOf = 0
        if (count % 2 == 0):
            middleOf = count//2 + 1
        else:
            middleOf = (count + 1)//2
        middle = head
        for i in range(middleOf - 1):
            middle = middle.next
        return middle

```
## Palindrome Linked List 

https://leetcode.com/problems/palindrome-linked-list/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        theMiddle = self.middle_list(head)
        AfterMiddle = self.reverse_list(theMiddle.next)
        res = True
        theMiddle = head
        After = AfterMiddle
        while res and After is not None:
            if theMiddle.val != After.val:
                res = False
            theMiddle = theMiddle.next
            After = After.next
        return res
    def reverse_list(self, head):
        theFirst = head
        if not theFirst or not theFirst.next:
            return theFirst
        theFirst.next, now, before = None, theFirst.next, theFirst
        while (now.next != None):
            now.next, now, before = before, now.next, now
        now.next = before
        return now
    def middle_list(self,head):
        eachOne = head
        divTwo = head
        while eachOne.next is not None and eachOne.next.next is not None:
            eachOne = eachOne.next.next
            divTwo = divTwo.next
        return divTwo

```
## Merge Two Sorted Lists 

https://leetcode.com/problems/merge-two-sorted-lists/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = tmpList = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tmpList.next = l1
                l1 = l1.next
            else:
                tmpList.next = l2
                l2 = l2.next
            tmpList = tmpList.next
        tmpList.next = l1 or l2
        return newList.next

```
## Remove Nth Node From End of List 

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head
        for i in range (n):
            first = first.next
        if not first: return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head

```
## Linked List Cycle II 

https://leetcode.com/problems/linked-list-cycle-ii/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None

```
## Linked List Cycle 

https://leetcode.com/problems/linked-list-cycle/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

```
## Reorder List 

https://leetcode.com/problems/reorder-list/

```python
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        fast, slow = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        middle = slow
        before = None
        while middle:
            middle.next, middle, before = before, middle.next, middle
        middlehead = before
        first = head
        while middlehead.next:
            swap = first.next
            first.next = middlehead
            first = swap

            swap = middlehead.next
            middlehead.next = first
            middlehead = swap

```
## Intersection of Two Linked Lists 

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        lenA = 0
        while curA:
            lenA = lenA + 1
            curA = curA.next
        curB = headB
        lenB = 0
        while curB:
            lenB = lenB + 1
            curB = curB.next
        if lenA > lenB:
            for i in range(lenA-lenB):
                headA = headA.next
        else:
            for i in range(lenB-lenA):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

```
## Sort List 

https://leetcode.com/problems/sort-list/

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        list = []
        current = head
        while (current):
            list.append(current.val)
            current = current.next

        list.sort() #tim sort = merge sort

        current = head
        for num in list:
            current.val = num
            current = current.next
        return head

```
