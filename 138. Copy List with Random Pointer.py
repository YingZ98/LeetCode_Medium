#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        while cur:
            next = cur.next
            tmp = Node(val = cur.val, next = next, random = None)
            cur.next = tmp
            cur = next
        cur = head
        while cur:
            cur.next.random = cur.random.next if  cur.random else None
            cur = cur.next.next
        cur = head
        newHead = head.next
        while cur:
            tmp = cur.next
            cur.next = tmp.next
            cur = cur.next
            tmp.next= cur.next if cur else None
        return newHead

