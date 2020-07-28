#!/usr/bin/env python
# coding: utf-8

# In[25]:


port1={21:"FTP",22:"SSH",23:"TELNET",80:"HTTP"}
PORT2={}
PORT2={port1[i]:i for i in port1}
print(PORT2)
    


# In[13]:


list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
for i in list1:
    x=sum(i)
    list2.append(x)
print(list2)


# In[24]:


l1=[(1,2,3),[1,2],["a","hit","less"]]
l2=[]
for i in l1:
    for j in i:
        l2.append(j)
print(l2)

