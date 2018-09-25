import numpy as np

a = np.array([[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29],[30,31,32,33,34,35]])

b = a.reshape(36)
print(b)

print(a[2:4,2:4])

s = 'abcdefghijklmn'


def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    count = 1
    temp = 1
    sub= ""+s[0]
    f = 0

    # for i in range(1, len(s)):


    #print(sub)
    #print(s[::3])

lengthOfLongestSubstring(s)

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


for person in people:
    #print(person.split()[0])
    print(person.split()[0]+ '__' +person.split()[-1])

add = lambda x,y,z: x+y
print(add(3,5,6))



#option 1
#for person in people:
#    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
# list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))


my_list = []
for number in range(0,1000):
    if number % 2 == 0:
        my_list.append(number)

#print(my_list)

my_list = [number for number in range(0,1000) if number % 2 == 0]
print(my_list)
print(people[1:])

import numpy as np

mylist = [1,2,3]
x = np.array(mylist)
y = np.array([7,8,9])

m = np.array([[7,8,9], [10,11,12]])
print(m)
print(m.shape)

n = np.arange(0,30,2)
print(n.shape)

n1 = n.reshape(3,5)
n2 = n.resize(3,5)

print(n1)
print(n.resize(3,5))

r = np.arange(36)
r.resize((6,6))
print(r)

import pandas as pd

s = pd.Series(np.random.randint(0,5,20))
print(s)

import timeit

print timeit.timeit(setup= 'from math import sqrt', stmt = mycode, number = 10000)





