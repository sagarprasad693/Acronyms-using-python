#!/usr/bin/env python
# coding: utf-8

# In[1]:


user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)


# In[ ]:




