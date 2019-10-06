#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        p = []        i = 0
        for i in path:
            if i =='.' or i=='':
                continue
            elif i=='..': 
                if len(p) > 0:p.pop()
            else: 
                p.append(i)
        return "/" + "/".join(p)

