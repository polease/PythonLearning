#%%  Basic Operations
print(2**3)
print(4/3)
4//3
print(4//3)
print(float(3))
"print(len(385)"
print("hippo" *12 )
print(type(133))
print("hello from {} there is a great {}, haha".format("lin","join"))

#%%

#Indentation

#no ;, no (), no {}

# comments
"""dfasdf
"""


# no (
# with :
# elif => else if
if 100> 99:
    print("there you are")
elif 100 > 101:
    print("again")
else:
    print("oops")


# boolean
# and or not


a = 10
print(a)
a = "hello"
print(a)

#anything convert to float
anything = "1093"
score = float(anything)

#%% 
#min, max(a,b,c,d)

#List => Array/IList
list = [0,"helloindex1",2,3,4]
print(list[0])
print(list[1])
print(list[-1])
 


# slice array
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[6:9]) 
print(months[2:]) 
print('January' in months)

# min,max,sum,sorted
print(len(months))
print(min(months))
print(max(months))
print(sorted(months))
print("+".join(months))

months[:2] = [0,1]
print(months)

months.append("hello")
print(months)

for month in months:
    print(month)

print( range(len(months)))
for i in range(len(months)):
    print(i)


while i < len(months):
    print(i)
    i+=1

# set()
countries = ["USA","CHINA","INDIA","USA","CHINA"]
print(len(countries))
countries_set =set(countries)
print(len(countries_set))
countries_set.add("RUSSIA")

# dictionary
zips = {92078:"san marcos",92009:"carlsbad",91001:"el segundo"}
cityname = zips[92078]
print(92078 in zips)
try:
    non_existing_city = zips[92111] #this should throw exception
except:
    print('encounter exception')
non_existing_city = zips.get(92011)
print(non_existing_city)


#tuples (immutable)
gps= (13.2323,200.20002)
print(gps)
latitude, longtitude = gps
print(latitude,longtitude)
 

def boundary(items):
    return min(items),max(items)

items = [7,2,9,0,4]
print(boundary(items))


#default parameter
def boundary(items,allowNegative = True):  
    if(allowNegative):  
        return min(items),max(items)
    else:
        new_items = []
        for i in items:
            if i > 0:
                new_items.append(i)        
        return min(new_items),max(new_items)


# variable scope
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs
try:
    buy_eggs()
    print(egg_count)
except:
    print("have error, can't access egg_count")


# file and with
f = open("sample.txt")
print(f.read())
f.close()
f = open("sample.txt",mode='w')
f.write("hello again")
f.close()

with open("sample.txt") as f:
    text = f.read() 
    print("{} from inside".format(text))

print("{} from outside".format(text))
 


# import
import math
result = math.exp(3)
print(result)

# import my own module
import mymodule
mymodule.hello("there")

from mymodule import hello
hello("again haha")


print(mymodule)

import mymodule as my
my.hello("3rd times")

import random
print(random.choice(countries))
print(random.sample(countries,2))


#lib list

#requirements.txt
#pip install -r requirements.txt




def continue_crawl(search_history,target_url):
    return not(target_url == search_history[-1] or len(search_history) > 25 or target_url in search_history)