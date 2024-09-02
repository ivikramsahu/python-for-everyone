#Tuples

#Tuples are used to store multiple items in a single variable.

name = ("John", "Jane", "Jack")

name[-1]
name.index("Jane")

len(name)

print("Jane" in name)
print(name[0:2])
print(sorted(name))

#Dictionaries
"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
"""

dog = {"name": "Roger", "age": 8, "color": "green"}
print(dog['age'])
dog['name'] = "scooby"

print(dog.get("plays", "ball"))
print(dog.pop("name"))
print("color" in dog)
dog["food"] = "meat"

dogCopy = dog.copy()
print(dog)

#Sets
"""
Sets are used to store multiple items in a single variable. Sets has unique items
A set is a collection which is unordered, unchangeable*, and unindexed.
"""

name = {"John", "Jane", "Jack"}
name2 = {"Jane", "Jack", "Jill"}

intersect = name & name2
print(intersect)
mod = name | name2  # -, >, len, <
print(mod)

#Functions
"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""


def hello1(name, age):
  print('Hello! ' + name + ", you are " + str(age) + " years old!")


hello1("Ricky", 5)


def change(value):
  value = 2
  return value

val = 1
change(val)
print(val)

def hello(name):
  if not name:
    return
  print('Hello ' + name + '!')

hello("Vikram")

#Nested Functions

def talk(phrase):
  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)

talk('I am going to buy the milk')

def count():
  count = 0

  def increment():
    nonlocal count
    count = count + 1
    print(count)

  increment()

count()

#Closures
"""
A closure is a function object that remembers its lexical environment even when executed in a different context.
"""
def counter():
  count = 0

  def increment():
    nonlocal count
    count = count + 1
    return count

  return increment

increment = counter()

print(increment()) #1
print(increment()) #2
print(increment()) #3

#objects
"""
All the objects in Python are derived from a built-in object class called object.
"""
age = 8
print(age.real)
print(age.imag)
print(age.bit_length())

items = [1, 2]
items.append(3)
items.pop()
print(id(items))

#Loops
"""
Loops are used to repeat a sequence of instructions.
There are two types of loops in Python: while and for.
"""
condition = True
while condition == True:
  print("The condition is True")
  condition = False


count = 0
while count < 10:
  print("The condition is true")
  count += 1

items = [1,2,3,4,5]
for i in enumerate(items):
  print(i[1])

#breaK and continue

for item in items:
  if item == 2:
    continue
  print(item)
