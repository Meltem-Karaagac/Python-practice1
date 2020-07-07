#!/usr/bin/env python
# coding: utf-8

# In[3]:


year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("True")  
       else:  
           print("False")  
   else:  
       print("True")  
else:  
   print("False") 


# In[2]:


print(set('listen to the voice of enlisted'))


# In[11]:


student_ages = {"Harry": 29,
                "Clark": 32,
                "Peter": 22,
                "Bruce": 36
                }

print(student_ages["Clark"])
print(student_ages["Clark"])
print(student_ages["Clark"])
print(student_ages["Clark"])


# In[8]:


grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
print(grocer[0],grocer[1][1][0])


# In[12]:


grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
print(grocer[1][1][1])


# In[2]:


numbers = {}

numbers['x'] = 12
numbers['y'] = 4
numbers.update({'z': 3})

print(numbers['x'] + numbers['y'] + numbers['z']**2)


# In[12]:


numbers_10 = [10, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_10.insert(1,20)
print(numbers_10)


# In[11]:


fruits_vege
tables = ["fruit", "vegetable", ["apple", "banana", ["mango", "avocado"]], ["spinach", "broccoli"]]
print((fruits_vegetables)[3][0])


# In[5]:


family = { 'name 1' : 'baba',
' name 2'  : 'anne', 
'name 3' : 'cocuk', }
print(family)


# In[ ]:




