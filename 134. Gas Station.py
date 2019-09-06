#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum = 0
        k = 0
        total = 0
        for i in range(0, len(gas)):
            sum += gas[i] - cost[i]
            if sum < 0:
                k = i + 1
                sum = 0
            total += gas[i] - cost[i]
        
        if total < 0:
            return -1
        else:
            return k

