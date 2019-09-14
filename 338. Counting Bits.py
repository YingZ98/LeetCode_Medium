#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0] * (num + 1)
        ans[0] = 0
        for i in range(1, num + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans 

