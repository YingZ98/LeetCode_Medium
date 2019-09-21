#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [0] * 38
        t[0], t[1], t[2] = 0, 1, 1
        for i in range(3, n+1):
            t[i] = t[i-1] + t[i-2] + t[i-3]
        return t[n]

