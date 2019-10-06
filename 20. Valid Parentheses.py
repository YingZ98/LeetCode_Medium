#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isValid(self, s: str) -> bool:
        temp=["-"]
        for c in s:
            if c in "([{":
                temp.append(c)
            if c ==")":
                if temp[-1]=="(":
                    temp.pop()
                else:
                    return False
            if c =="]":
                if temp[-1]=="[":
                    temp.pop()
                else:
                    return False
            if c =="}":
                if temp[-1]=="{":
                    temp.pop()
                else:
                    return False
        return len(temp)==1

