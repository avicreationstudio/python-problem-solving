# problems

## `reverse the linked list`

### problem statement

<https://leetcode.com/problems/reverse-linked-list/>

Given the head of a singly linked list, reverse the list, and return the reversed list.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
```

solution

```python
class Solution:
    def reverse(self):
        pre = None
        cur = self.head
        nxt = None
        while cur != None:
            nxt = cur.next
            cur.next = pre 
            pre = cur 
            cur = nxt 
        self.head = pre
```
