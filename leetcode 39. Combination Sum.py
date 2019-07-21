#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 39. Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        List=[]
        res=[]
        def com(res,candidates,target):
            if target==0:
                List.append(res)
            else:
                if len(candidates)==0:
                    return
                newtarget=target - candidates[0]
                newcandidates=[]
                for i in candidates:
                    if i <=newtarget:
                        newcandidates=newcandidates+[i]
                com(res+[candidates[0]],newcandidates,newtarget)
                com(res,candidates[1:],target)
        com(res,candidates,target)
        return List

