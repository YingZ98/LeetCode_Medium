#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        res = [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                outl = mid
                outr = mid
                res = [mid, mid]
                while outl > 0 and nums[outl - 1] == nums[outl]:
                    outl = outl - 1
                    res[0] = outl
                while outr < n - 1 and nums[outr] == nums[outr + 1]:
                    outr = outr + 1
                    res[1] = outr
                return res
            else:
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1
        return res
        

