#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums,0,len(nums)-1,target)
    
    def helper(self,nums,low,high,target):
        if low>high:
            return -1
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        
        # 如果右左半部分是有序数列
        if nums[mid]<nums[high]:
            if nums[mid] < target and target <= nums[high]: #如果target位于右半部分,则继续二分查找
                return self.helper(nums,mid+1,high,target)
            else:
                return self.helper(nums,low,mid-1,target)  #否则去找左半部分  

        # 进行左半部分的判断。
        else:
            if nums[low] <= target and target < nums[mid]:  #如果target位于左半部分有序数列中,则继续二分查找
                return self.helper(nums,low,mid-1,target)
            else:
                return self.helper(nums,mid+1,high,target)  

