#!/usr/bin/env python
# coding: utf-8

# In[6]:


num =input("Please enter a number :")
if num.isdigit() != True:
    print(("It is an invalid entry. Don`t use non-numeric, float or negative values!"))
else:
    num_list = list(num)
    i = 1
    total = 0
    while i <= (len(num_list)):
        total += int(num_list[i-1])**len(num_list)
        i += 1
    if int(num) == total:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number" )


# In[ ]:




