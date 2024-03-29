#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return right

