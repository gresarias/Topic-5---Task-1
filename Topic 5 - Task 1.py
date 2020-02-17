#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[2]:


pip install pandas


# In[3]:


pip install matplotlib


# In[4]:


pip install scipy


# In[1]:


pip freeze


# In[2]:


pip3 install --upgrade pip


# In[3]:


import math


# In[4]:


math.sqrt(25)


# In[5]:


math.pi


# In[6]:


import math as mt


# In[7]:


mt.sqrt(25)


# In[8]:


from numpy import random


# In[9]:


import numpy as np


# In[10]:


# uniform random numbers in [0,1]
dataOne = random.rand(5,5)


# In[11]:


np.mean(dataOne)


# In[12]:


mt.sqrt(np.mean(dataOne))


# In[13]:


mt.sqrt(datOne)


# In[14]:


mt.sqrt(np.mean(dataOne))


# In[15]:


print(dataOne)


# In[16]:


in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)


# In[17]:


print('Greivin Arias with Data Science')


# In[18]:


variableName = 25


# In[19]:


print(variableName)


# In[20]:


variableName1 = 'Greivin Arias'


# In[21]:


print(variableName1)


# In[22]:


type(variableName)


# In[23]:


variableName = 25.0


# In[24]:


type(variableName)


# In[25]:


varOne = 25


# In[26]:


varTwo = 25.0


# In[27]:


varThree = varOne + varTwo


# In[28]:


print(varThree)


# In[29]:


varTwo 'Hello''


# In[30]:


varTwo = 'Hello'


# In[31]:


varThree = varOne + varTwo


# In[32]:


listOne = [1,2,3,4,5]


# In[33]:


print(listOne)


# In[34]:


print(listOne[0:2])


# In[35]:


print(listOne[0,2])


# In[36]:


print(listOne[0:5])


# In[37]:


print(listOne[0:4])


# In[38]:


Tels = {'Jack': 4098, 'Sape': 4139}


# In[39]:


Tels['Jack']


# In[40]:


Nacimientos = {'Greivin': 1983, 'Cata'= 1988, 'Dani' = 2003, 'Floppy' = 2018, 'Matrimonio' = 2020}


# In[41]:


Nacimientos = {'Greivin':1983, 'Cata':1988, 'Dani':2003, 'Floppy':2018, 'Matrimonio':2020}


# In[42]:


math.gcd('Greivin', 'Cata')


# In[43]:


math.gcd(Nacimientos['Greivin'], Nacimientos['Cata'])


# In[44]:


math.dist(Nacimientos['Greivin'], Nacimientos['Cata'])


# In[45]:


math.dist(Nacimientos['Greivin'], Nacimientos['Cata'])


# In[46]:


math.cos(Nacimientos['Greivin'])


# In[47]:


math.log10(Nacimientos['Floppy'])


# In[48]:


math.sqrt(Nacimientos['Dani'])


# In[49]:


print(math.cos(Nacimientos['Greivin']))


# In[50]:


print9math.gcd(Nacimientos['Greivin'], Nacimientos['Cata'])0


# In[51]:


print(math.gcd(Nacimientos['Greivin'], Nacimientos['Cata']))


# In[52]:


print(math.log10(Nacimientos['Floppy']))


# In[53]:


print(math.sqrt(Nacimientos['Dani']))


# In[54]:


print(listOne)


# In[55]:


listOne.insert(6)


# In[56]:


listOne.insert(6,6)


# In[57]:


print(listOne)


# In[58]:


listOne.append(7)


# In[59]:


print(listOne)


# In[60]:


listOne.insert(0,0)


# In[61]:


print(listOne)


# In[62]:


listOne.remove(3)


# In[63]:


print(listOne)


# In[64]:


listOne([6])


# In[65]:


listOne.pop([6])


# In[66]:


listOne.pop


# In[67]:


print(listOne)


# In[68]:


listOne.count(2)


# In[69]:


listOne.append(2)


# In[70]:


print(listOne)


# In[71]:


listOne.count(2)


# In[72]:


listOne.sort


# In[73]:


print(listOne)


# In[74]:


listOne


# In[75]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


# In[76]:


fruits.count('apple')


# In[77]:


fruits.count('grape')


# In[78]:


fruits.index('banana')


# In[79]:


fruits.reverse()


# In[80]:


fruits


# In[81]:


fruits.append('grape')


# In[82]:


fruits


# In[83]:


fruits.sort()


# In[84]:


fruits


# In[85]:


fruits.pop()


# In[86]:


fruits.pop(4)


# In[87]:


fruits


# In[88]:


listOne.sort


# In[89]:


listOne


# In[90]:


#Collections.deque was designed to have fast appends and pops from both ends
from collections import deque


# In[91]:


queue = deque(["Floppy", "Greivin"])


# In[92]:


queue.append("Cata")


# In[93]:


queue.append("Dani")


# In[94]:


queue


# In[95]:


queue.popleft


# In[96]:


queue


# In[97]:


queue.popleft()


# In[98]:


queue.popleft()


# In[99]:


queue


# In[100]:


squares = []
for x in range(10):
    squares.append(x**2)


# In[101]:


squares


# In[102]:


squares = list(map(lambda x: x**2, range(10)))


# In[103]:


squares


# In[105]:


[(x, y) for x in [1,2,3] for y in [3,1,4]]


# In[106]:


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[107]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))


# In[108]:


combs


# In[109]:


vec = [-4, -2, 0, 2, 4]


# In[110]:


[x**2 for x in vec]


# In[111]:


[abs(x)*2 for x in vec]


# In[112]:


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


# In[113]:


mstrix


# In[114]:


matrix


# In[115]:


list(zip(*matrix))


# In[116]:


a = [-1,1,66.25,333,333,12345.5]


# In[117]:


del a[0]


# In[118]:


a


# In[119]:


del a[2:4]


# In[120]:


a


# In[121]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}


# In[122]:


basket


# In[123]:


the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")


# In[124]:


2+2


# In[125]:


50 -5*6


# In[126]:


(50-5*6)/4


# In[127]:


8/5


# In[128]:


17/3


# In[129]:


17//3


# In[130]:


17%3


# In[131]:


5*3+2


# In[132]:


5**2


# In[133]:


2**7


# In[134]:


width = 20
height = 5 * 9
width * height


# In[135]:


n


# In[136]:


4 * 3.75 - 1


# In[137]:


tax = 12.5 / 100
price = 100.50
price * tax


# In[138]:


price + _


# In[139]:


round (_,1)


# In[140]:


'spam eggs'  # single quotes


# In[141]:


'doesn\'t'  # use \' to escape the single quote...


# In[142]:


"doesn't"  # ...or use double quotes instead


# In[143]:


'"Yes," they said.'


# In[144]:


"\"Yes,\" they said."


# In[145]:


'"Isn\'t," they said.'


# In[146]:


print('"Isn\'t," they said.')


# In[147]:


s = 'First line.\nSecond line.'  # \n means newline


# In[148]:


s  # without print(), \n is included in the output


# In[149]:


print(s)


# In[150]:


print('C:\some\name')  # here \n means newline!


# In[151]:


print(r'C:\some\name')  # note the r before the quote


# In[152]:


print("""Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# In[153]:


3 * 'un' + 'ium' # 3 times 'un', followed by 'ium'


# In[154]:


'Py' 'thon'


# In[155]:


'Py' 'thon'


# In[156]:


text = ('Put several strings within parentheses '
        'to have them joined together.')


# In[157]:


text


# In[158]:


prefix = 'Py'


# In[159]:


prefix 'thon'  # can't concatenate a variable and a string literal


# In[160]:


prefix + 'thon'


# In[161]:


word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5


# In[162]:


word[0]  # character in position 0


# In[163]:


word[-1]  # last character


# In[164]:


word[-2]  # second-last character


# In[165]:


word[-6]


# In[166]:


word[0:2]  # characters from position 0 (included) to 2 (excluded)


# In[167]:


word[2:5]  # characters from position 2 (included) to 5 (excluded)


# In[168]:


word[0:2] + word[2:6]


# In[169]:


word[:2] + word[2:]


# In[170]:


word[:4] + word[4:]


# In[171]:


word[:2]   # character from the beginning to position 2 (excluded)


# In[172]:


word[4:]   # characters from position 4 (included) to the end


# In[173]:


word[-2:]  # characters from the second-last (included) to the end


# In[174]:


word[42]


# In[175]:


word[4:42]


# In[176]:


word[42:]


# In[177]:


word[0] = 'J'


# In[178]:


'J' + word[1:]


# In[179]:


word[:2] + 'py'


# In[180]:


s = 'supercalifragilisticexpialidocious'


# In[181]:


len(s)


# In[182]:


squares = [1, 4, 9, 16, 25]


# In[183]:


squaes


# In[184]:


squares


# In[185]:


squares[0]


# In[186]:


squares[-1]


# In[187]:


squares[-3:]


# In[188]:


squares[:]


# In[189]:


squares + [36, 49, 64, 81, 100]


# In[190]:


cubes = [1, 8, 27, 65, 125]  # something's wrong here


# In[191]:


cubes


# In[192]:


4 ** 3  # the cube of 4 is 64, not 65!


# In[193]:


cubes[3] =64


# In[194]:


cubes


# In[195]:


cubes.append(216)  # add the cube of 6


# In[196]:


cubes.append(7 ** 3)  # and the cube of 7


# In[197]:


cubes


# In[198]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# In[199]:


letters


# In[200]:


# replace some values
letters[2:5] = ['C', 'D', 'E']


# In[201]:


letters


# In[202]:


# now remove them
letters[2:5] = []


# In[203]:


letter


# In[204]:


letters


# In[205]:


# clear the list by replacing all the elements with an empty list
letters[:] = []


# In[206]:


letters


# In[207]:


letters = ['a', 'b', 'c', 'd']
len(letters)


# In[208]:


a = ['a', 'b', 'c']


# In[209]:


n = [1, 2, 3]


# In[210]:


x = [a, n]


# In[211]:


x


# In[212]:


x[0]


# In[213]:


x[0][1]


# In[214]:


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


# In[215]:


a, b = 0, 1
while a < 1000:
    print(a)
    a, b = b, a+b


# In[216]:


a, b = 0, 1
while a < 1000:
    print(a,b)
    a, b = b, a+b


# In[217]:


x = int(input("Please enter an integer: "))
Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# In[218]:


x = int(input("Please enter an integer: "))
Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

More


# In[219]:


x = int(input("Please enter an integer: "))


# In[220]:


x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

More


# In[221]:


x = int(input("Please enter an integer: "))
Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# In[222]:


x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# In[224]:


x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# In[225]:


x


# In[226]:


x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# In[227]:


x


# In[228]:


# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# In[229]:


# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


# In[230]:


# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# In[231]:


for i in range(5):
    print(i)


# In[232]:


range(5, 10)
   5, 6, 7, 8, 9


# In[233]:


range(5, 10)


# In[234]:


range


# In[235]:


range(10)


# In[236]:


print(range)


# In[237]:


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# In[238]:


print(range(10))


# In[239]:


sum(range(4))  # 0 + 1 + 2 + 3


# In[240]:


list(range(4))


# In[243]:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print('N=',n)
        print('X=',x)
        print(n, 'is a prime number')


# In[244]:


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


# In[ ]:


while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# In[ ]:


class MyEmptyClass:
    pass


# In[ ]:


def initlog(*args):
    pass   # Remember to implement this!


# In[ ]:


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[ ]:


fib(2000)


# In[ ]:


fib(2000)


# In[ ]:


2+2


# In[ ]:


print(variableName)


# In[1]:


print(variableName)


# In[12]:


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[3]:


fib(2000)


# In[4]:


f = fib


# In[5]:


f(100)


# In[6]:


fib(0)


# In[7]:


print(fib(0))


# In[16]:


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[17]:


fib(0)


# In[18]:


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


# In[19]:


f100 = fib2(100)


# In[20]:


f100


# In[21]:


fib2(1000)


# In[22]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[23]:


ask_ok


# In[24]:


ask_ok('Do you really want to quit?')


# In[25]:


ask_ok('OK to overwrite the file?', 2)


# In[26]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[27]:


def f(a, L=[]):
    L.append(a)
    return L


# In[28]:


print(f(1))


# In[29]:


print(f(2))


# In[30]:


print(f(3))


# In[31]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# In[32]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[33]:


parrot(1000)


# In[34]:


parrot(voltage=1000)


# In[35]:


parrot(voltage=1000000, action='VOOOOOM') 


# In[36]:


parrot(action='VOOOOOM', voltage=1000000) 


# In[37]:


parrot('a million', 'bereft of life', 'jump')


# In[38]:


parrot('a thousand', state='pushing up the daisies')


# In[39]:


parrot()   


# In[40]:


parrot(voltage=5.0, 'dead')


# In[41]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[42]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# In[46]:


def standard_arg(arg):
    print(arg)


# In[48]:


def pos_only_arg(arg, /):
    print(arg)


# In[49]:


def kwd_only_arg(*, arg):
    print(arg)


# In[50]:


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# In[51]:


standard_arg(2)


# In[52]:


standard_arg(arg=2)


# In[53]:


pos_only_arg(1)


# In[54]:


pos_only_arg(arg=1)


# In[55]:


kwd_only_arg(3)


# In[56]:


kwd_only_arg(arg=3)


# In[57]:


ef foo(name, **kwds):
    return 'name' in kwds


# In[58]:


def foo(name, /, **kwds):
    return 'name' in kwds
>>> foo(1, **{'name': 2})
True


# In[59]:


def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):


# In[60]:


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[61]:


def concat(*args, sep="/"):
    return sep.join(args)


# In[71]:


concat("earth", "mars", "venus")


# In[72]:


concat("earth", "mars", "venus", sep=".")


# In[68]:


def concat2(*args, sep="-Next-"):
    return sep.join(args)


# In[70]:


concat2("earth", "mars", "venus")


# In[73]:


list(range(3, 6)) # normal call with separate arguments


# In[74]:


args = [3, 6]


# In[75]:


list(range(*args))            # call with arguments unpacked from a list


# In[76]:


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


# In[77]:


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}


# In[78]:


parrot(**d)


# In[79]:


def make_incrementor(n):
    return lambda x: x + n


# In[80]:


f = make_incrementor(42)


# In[81]:


f(0)


# In[82]:


f(2)


# In[83]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]


# In[84]:


pairs.sort(key=lambda pair: pair[1])


# In[85]:


pairs


# In[86]:


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


# In[87]:


print(my_function.__doc__)


# In[88]:


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


# In[89]:


f('spam')


# In[90]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


# In[91]:


fruits.count('apple')


# In[92]:


fruits.count('tangerine')


# In[93]:


fruits.index('banana')


# In[94]:


3
fruits.index('banana', 4)  # Find next banana starting a position 4


# In[95]:


fruits.reverse()


# In[96]:


fruits


# In[97]:


fruits.append('grape')


# In[98]:


fruits


# In[99]:


fruits.sort()


# In[100]:


fruits


# In[101]:


fruits.pop


# In[102]:


fruits.pop()


# In[103]:


fruits


# In[104]:


stack = [3,4,5]


# In[105]:


stack.append(6)


# In[106]:


stack.append(7)


# In[107]:


stack


# In[108]:


stack.pop()


# In[109]:


stack.pop()


# In[110]:


from collections import deque


# In[111]:


queue = deque(["Greivin", "Cata", "Floppy"])


# In[112]:


queue.append("Dani")


# In[113]:


queue.popleft()


# In[114]:


queue.popleft()


# In[115]:


queue


# In[116]:


squares = []
for x in range(10):
    squares.append(x**2)


# In[117]:


squares


# In[118]:


squares = list(map(lambda x: x**2, range(10)))


# In[119]:


squares = [x**2 for x in range(10)]


# In[120]:


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[121]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))


# In[122]:


combs


# In[123]:


vec = [-4, -2, 0, 2, 4]


# In[124]:


[x*2 for x in vec]


# In[125]:


[x*2*2 for x in vec]


# In[126]:


[x**2 for x in vec]


# In[127]:


[x for x in vec if x >= 0]


# In[128]:


[abs(x) for x in vec]


# In[129]:


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']


# In[130]:


[weapon.strip() for weapon in freshfruit]


# In[131]:


[(x, x**2) for x in range(6)]


# In[132]:


[x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]


# In[133]:


[x, x**2 for x in range(6)]


# In[134]:


vec = [[1,2,3], [4,5,6], [7,8,9]]


# In[135]:


[num for elem in vec for num in elem]


# In[136]:


from math import pi


# In[137]:


[str(round(pi, i)) for i in range(1, 6)]


# In[138]:


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


# In[139]:


[[row[i] for row in matrix] for i in range(4)]


# In[140]:


transposed = []


# In[141]:


for i in range(4):
    transposed.append([row[i] for row in matrix])


# In[142]:


transposed


# In[143]:


transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


# In[144]:


transposed


# In[145]:


list(zip(*matrix))


# In[146]:


a = [-1, 1, 66.25, 333, 333, 1234.5]


# In[147]:


del a[0]


# In[148]:


a


# In[149]:


del a[2:4]


# In[150]:


a


# In[151]:


del a[:]


# In[152]:


a


# In[153]:


del a


# In[154]:


a


# In[155]:


t = 12345, 54321, 'hello!'


# In[156]:


t[0]


# In[157]:


t


# In[158]:


u = t, (1, 2, 3, 4, 5)


# In[159]:


u


# In[160]:


t[0] = 8888


# In[161]:


v = ([1, 2, 3], [3, 2, 1])


# In[162]:


v


# In[163]:


empty = ()


# In[164]:


singleton = 'hello',    # <-- note trailing comma


# In[165]:


len(empty)


# In[166]:


len(singleton)


# In[167]:


singleton


# In[168]:


x, y, z = t


# In[169]:


t


# In[170]:


x


# In[171]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}


# In[172]:


basket


# In[173]:


orange in basket


# In[174]:


'orange'in basket


# In[175]:


'crabgrass' in basket


# In[176]:


a = set ('abracadabra')


# In[177]:


b = set('alacazom')


# In[178]:


b = set('alacazam')


# In[179]:


a


# In[180]:


a-b


# In[181]:


a | b 


# In[182]:


a & b


# In[183]:


a ^ b


# In[184]:


a = {x for x in 'abracadabra' if x not in 'abc'}


# In[185]:


a


# In[186]:


tel = {'jack': 4098, 'sape': 4139}


# In[187]:


tel['guido'] = 4127


# In[188]:


tel


# In[189]:


tel['jack']


# In[190]:


del tel['sape']


# In[191]:


tel


# In[192]:


tel['irv'] = 4127


# In[193]:


tel


# In[194]:


list(tel)


# In[195]:


sorted(tel)


# In[196]:


'guido'in tel


# In[197]:


'jack'in tel


# In[198]:


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


# In[199]:


{x: x**2 for x in (2, 4, 6)}


# In[200]:


dict(sape=4139, guido=4127, jack=4098)


# In[201]:


knights = {'gallahad': 'the pure', 'robin': 'the brave'}


# In[202]:


for k, v in knights.items():
    print(k, v)


# In[203]:


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# In[204]:


questions = ['name', 'quest', 'favorite color']


# In[205]:


answers = ['lancelot', 'the holy grail', 'blue']


# In[206]:


for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# In[207]:


for i in reversed(range(1, 10, 2)):
    print(i)


# In[208]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']


# In[209]:


for f in sorted(set(basket)):
    print(f)


# In[210]:


import math


# In[ ]:





# In[211]:


raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]


# In[212]:


filtered_data = []


# In[213]:


for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)


# In[214]:


filtered_data


# In[215]:


string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'


# In[216]:


non_null = string1 or string2 or string3


# In[217]:


non_null


# In[219]:


(1, 2, 3) < (1, 2, 4)


# In[220]:


[1, 2, 3] < [1, 2, 4]


# In[221]:


'ABC' < 'C' < 'Pascal' < 'Python'


# In[222]:


(1, 2, 3, 4) < (1, 2, 4)


# In[223]:


(1, 2) < (1, 2, -1)


# In[224]:


(1, 2, 3) == (1.0, 2.0, 3.0)


# In[225]:


(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)


# In[ ]:




