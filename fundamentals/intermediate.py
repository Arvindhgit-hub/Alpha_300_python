#tuple====================================
mytuple = ("max",28,"boston")
print(mytuple)
item = mytuple[0]
print(item)

for i in mytuple:
    print(i)
if "max" in mytuple:
    print("yes")
else:
    print("no")
print(mytuple.count('max'))
print(mytuple.index(28))
a = (1,2,3,4,5)
b = a[0:4]
my_list = list(mytuple)
print(my_list)
a = (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
print(b)
name , age , city = mytuple
print(name)
print(age)
print(city)
import sys
print(sys.getsizeof(my_list),"bytes")
import timeit 
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))
#dictionary=====================================
mydict = {"name":"max","age": 28 ,"city":"newyork"}
print(mydict)
mydict2 = dict(name="mary",age=27,city="boston")
print(mydict2)
mydict["email"] = "max@xyz.com"
print(mydict)
mydict.pop("age")
print(mydict) 
mydict_cpy = mydict
print(mydict_cpy)
my_dict = {3:9,6:36,9:81}
print(my_dict)
my_tuple = (8,7)
mydict = {mytuple: 15}
print(mydict)
#set=====================================
myset = {1,2,3,1,2}
print(myset)
myset = set("Hello")
print(myset)
myset1 = set()
myset1.add(1)
myset1.add(2)
myset1.add(3)
myset1.remove(2)
print(myset1)
myset1.discard(3)
myset.clear()
odds = {1,3,5,7,9,}
evens = {0,2,4,6,8,}
primes = {1,2,3,5,7}
un = odds.union(evens)
print(un)
intn = odds.intersection(evens)
print(intn)
setA = {1,2,3,4,5,6,7,8}
setB = {1,2,3,10,11,12}
diff = setB.difference(setA)
print(diff)
diff1 = setB.symmetric_difference(setA)
print(diff1)
setA.intersection_update(setB)
print(setA)
a = frozenset([1,2,3,4])
#string=========================
my_string = 'hello world'
char = my_string[0]
print(char)
substr = my_string[ 2:7]
print(substr)
greet = "helloo"
name = "SPYDY"
sentence = greet +" "+ name
print (sentence)
print(my_string.find('o'))
print(my_string.count('p'))
print(my_string.replace('e','o'))
mystr_list = my_string.split()
print(mystr_list)
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
text = "programming"

for char in set(text):
    print(char, text.count(char))    
var = "Tom"
mystr = "the variable is %s " % var 
print(mystr)   
#collections==================================
from collections import Counter
a = "aaaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))
from collections import namedtuple
point = namedtuple('point','x,y')
pt = point(1,-4)
print(pt)
from collections import OrderedDict
ordered_dict = OrderedDict
ordered_dict['a'] = 1
ordered_dict['b'] = 2

print(ordered_dict)
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
from collections import deque
de= deque()
de.append(1)
de.append(2)
de.appendleft(3)
print(de)
de.popleft()

#itertools===========================
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b,repeat=2)
print(list(prod))
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print()
from itertools import combinations , combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a)
print(list(comb))
a = [1,2,3,4,]
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

#Lambda===================================
add10= lambda x: x+10
print(add10(5))

points2D = [{1,2},{15,1},{5,-1},{10,4}]
points2D_sorted = sorted(points2D)
print(points2D)
a = [1,2,3,4,5]
b = map(lambda x: x+2, a)
print(list(b))
b = filter(lambda x: x%2==0,a)
print(list(b))
#exceptions error=======================
try:
    a = 5 / 0
except ZeroDivisionError:
    print('an error happend')
#logging==================================
import logging
import logging.config
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
logging.config.fileConfig('logging.conf')
#JSON======================================
import json 
person ={"name":"john","age":30,"city":"NewYork","hasChildren":False,"titles":["engineer","Programmer"]}
personJSON = json.dumps(person, indent = 4,sort_keys=True)
print(personJSON)
with open('person.json','w') as file:
    json.dump(person,file,indent=4)

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
user = User('Max',27)
def encode_user(o):
    if isinstance(o,User):
        return{'name': o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError('Obeject of type User is not JSON serializable')
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self,o):
        if isinstance(o,User):
            return{'name': o.name,'age':o.age,o.__class__.__name__:True}
        return JSONEncoder.default(self,o)
userJSON = json.dumps(user,default=encode_user)
print(userJSON)    

    