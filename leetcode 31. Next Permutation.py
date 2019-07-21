#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 31. Next Permutation
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(n-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        left, right = i, n-1
                        while left < right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1    
                        return
        nums.sort()

