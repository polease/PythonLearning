
# coding: utf-8

# # Transition from .Net to Python

# ## Meta
# |time|audience|link|content abstract|
# |------|------| ------|------|
# | 2:00 | .net/C# developer would like to learn machine learning and python programming | https://github.com/polease/PythonLearning/blob/master/PythonForDotNet.ipynb | Learn the basic about python include type, coding style and the difference or similiarity between .net development and python |
# 

# ## Agenda
# * [Basic Types](#Basic-Types)
# * [Basic Operations](#Basic-Operations)
# * [Basic functions](#Basic-Functions)
# * [Coding Style](#Coding-Style)
# * [Data Structure](#Data Structure)
# * [Class](#Class)
# * [Common Libs](#Common-libs)
# * Tools
# 
# ___

# ### Basic Types
# * int
# * float
# * str
# * bool
# * object

# In[105]:


type(1)


# In[106]:


type("hello")


# In[107]:


type(1.5)


# In[108]:


type(False)


# In[109]:


type(object())


# In[110]:


# convert type
float(1)


# In[111]:


# parse string
anything = "1093"
score = float(anything)
score


# ---

# ### Basic Operations

# In[112]:


# = + - * / %, same as C#
1 + 3 % 2 * 2


# In[113]:


# / will convert int to float
3/2


# In[114]:


# divide and round
3//2


# In[115]:


# power
3**3


# In[116]:


# string multiplication
"hello" * 3


# In[117]:


# and, or, not = C# &&, || , !
not ((1 == 2) or (3 == "3") and (4 == 4))


# ---

# ### Basic Functions

# In[118]:


# Get type of object = typeof in C#
type(1.5)


# In[119]:


# write output to console = console.writeline in C#
print("hello world from {}, how cool is that {}".format("lin","!"))


# In[120]:


len("hello world")


# #### Tuple
# 
# Tuple is immutable

# In[121]:


# Tuple
gps= (13.2323,200.20002)
print(gps)
print(type(gps))


# In[122]:


# tuple assignment
latitude, longtitude = gps
print(latitude,longtitude)


# ---

# ### Data Structure
# 
# Python is a dynamic programming language, everything is derived from object including basic type int/float/str. Following are the common used data types.
# 
# * List
# * Set
# * Dictionary
# * Range
# * Tuple

# #### List
# List is the most powerful built-in data strucure, it's the foundation of python data science project.
# 
# *Python List = C# Array + List<> + more*
# 

# In[123]:


#Python list can store anything(object)
list = [0,"helloindex1",2,3,4]
print(type(list))
list


# In[124]:


# powerful indexing and reverse indexing
print(list[0])
print(list[1])
print(list[-1])


# In[125]:


# powerful slicing
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[6:9]) 
print(months[2:]) 


# In[126]:


# powerful built-in function : min, max, len, sorted
# min,max,sum,sorted
print(len(months))
print(min(months))
print(max(months))
print(sorted(months))
print("+".join(months))


# In[127]:


# mutliple item editing
months[:2] = [0,1]
print(months)


# In[128]:


# add item
months.append("great")
print(months)


# In[129]:


# len of the array
len(months)


# #### Set
# 
# Unique set of items, no duplicate, not ordered
# 

# In[130]:


countries = ["USA","CHINA","INDIA","USA","CHINA"]
print(len(countries))
countries_set =set(countries)
print(len(countries_set))


# In[131]:


# add item to set
countries_set.add("RUSSIA")
countries_set


# #### Dictionary
# 
# Similar to c# dictionary

# In[132]:


zips = {92078:"san marcos",92009:"carlsbad",91001:"el segundo"}
cityname = zips[92078]
cityname


# #### Range
# 
# widely used in for loop

# In[133]:


# range function to generate a list of numbers
print(range(20))


# ---

# ### Coding Style
# 
# **Simplicity**  
# * no ";" at the end of line
# * no "{}" to capture the scope of function, if/else, try/catch and block of code
# * no "()" to if, for, while 
# * **no type declaration** (this is hard to get around from .net developer)
# 
# **Different**
# * use # to comment code
# * use """ for function specification
# * use ":" and indentation to indicate starting of the scope
# * use "elif" instead of "else if"
# * " or ' mean the same thing to declare str
# 
# 
# 

# In[134]:


if 100> 99:
    print("there you are")
elif 100 > 101:
    print("again")
else:
    print("oops")


# In[135]:


# for loop
for month in months:
    print(month)


# In[136]:


# there is no index version of for loop, so here is the mimic version 
for i in range(len(months)):
    print(i)


# In[137]:


# while loop
i = 0
while i < len(months):
    print(i)
    i+= 1


# In[138]:


try:
    non_existing_city = zips[92111] #this should throw exception
except:
    print('encounter exception')
non_existing_city = zips.get(92011)
print(non_existing_city)


# #### function 
# 
# * no public, private
# * no parameter type
# * no return signature type
# * default return None

# In[139]:


def print_numbers(items,allowNegative = True):  
    output_items = items
    if not allowNegative:  
        output_items = []
        for i in items:
            if i > 0:
                output_items.append(i)   
    
    for i in output_items:
        print(i)      

items = [13,99,-10,32]
print_numbers(items,False)
print_numbers(items)


# In[140]:


def boundary(items):
    return min(items),max(items)

items = [7,2,9,0,4]
print(boundary(items))


# ---

# ### Common Libs
# 
# Python library is orgnized by module, each module can use import to include into your code. We will explore how to conduct operation on below areas via libs/modules.
# 
# * Math
# * Random
# * Date
# * File
# * Network
# 
# 

# #### Import
# 
# Import package in python is using import keyword, or from module import xx, this in C# is via using.

# In[141]:


import math
result = math.exp(3)
print(result)


# In[142]:


# import my own module
import mymodule
mymodule.hello("there")

print(mymodule)


# In[143]:


# import object from my module
from mymodule import hello
hello("again haha")


# In[144]:


# import with alias name
import mymodule as my
my.hello("3rd times")


# #### Random

# In[145]:


import random
rand = random.randint(0,100)
rand


# In[146]:


random.sample(countries,2)


# In[147]:


random.choice(countries)


# #### Date
# 
# Python has a very good support of datetime and timezone management via datetime module. It includes:
#     timedelta,    tzinfo,    time,    date,        datetime

# In[148]:


from datetime import date
date.today()


# In[149]:


d = date(1988,8,8)
d


# In[150]:


d2 = date(2001,3,3)
(d2-d).days


# #### File
# 
# Reading/Write file in Python is very easy, no stream object, just file itself can read and write.
# 

# In[151]:


f = open("sample.txt")
print(f.read())
f.close()
f = open("sample.txt",mode='w')
f.write("hello again")
f.close()


# In[152]:


with open("sample.txt") as f:
    text = f.read() 
    print("{} from inside".format(text))

# below line of code still can access text variable
print("{} from outside".format(text)) 


# #### Network
# 
# Network request is also relative simple and clean in python.
# 
# 

# In[153]:


import requests
resp = requests.get("http://www.google.com")
resp.text[:100]


# ## Classes
# Python is advanced dynamics programing language. It has very good support of class and object oriented programming.
# 
# 

# In[154]:


from datetime import date
from datetime import timedelta

class Car:
    mileage = 0
    make = "toyota"
    model = 'prius'
    last_mainteinance_date = date
    
    # construction function = C# public Car(xxx)
    def __init__(self, mileage,make,model,last_mainteinance_date = date.today()):
        self.mileage = mileage
        self.make = make
        self.model = model
        self.last_mainteinance_date = last_mainteinance_date
    
    def next_mainteinance(self):
        next_milage = (self.mileage // 5000 + 1) * 5000
        next_date = self.last_mainteinance_date + timedelta(days=90)
        return next_milage,next_date
    
    # = c# ToString
    def __str__(self): 
        return ",".join([str(self.mileage),self.make,self.model,str(self.last_mainteinance_date)])

    


# In[155]:


my_car = Car(23000,"honda","accord") # = C# new Car(XXX)
my_car.model


# In[156]:


my_car


# In[157]:


print(my_car)


# In[158]:


my_car.next_mainteinance()


# # Resources
# |time|audience|link|content abstract|
# |------|------| ------|------|
# | 10:00 | anyone even without programming experience |https://www.udacity.com/course/introduction-to-python--ud1110 | An detail courseware to lear python from scratch, it also have labs, as always high quality udacity course |
# | 1:00 |C#/Dot net developer | https://www.youtube.com/watch?v=6TSvV2rsQHg | An one hour side by side comparision between C# and python |
