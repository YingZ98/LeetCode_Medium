#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class RecentCounter:

def __init__(self):
    self.li=[]


def ping(self, t):
    self.li.append(t)
    index=0
    while(True):
        if(self.li[index]<t-3000):
            index+=1
        else:
            self.li=self.li[index:]
            break
    return len(self.li)

