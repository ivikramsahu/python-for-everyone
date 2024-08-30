#variable

name = int("20")
age = float(39)

print(name)

print(isinstance(name,str))
print(isinstance(age,float))

#expresion

print(8 ** 2)

#datatypes
"""
string
int
float
complex
bool
list
tuple
range
dict
set
"""

#arithmetic operators

"""
1 + 1 #2
2 - 1 #1
2 * 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
5 // 2 #2
"""

#comparison operators
""" 
a = 1
b = 2

a == b #false
a != b #true
a > b #false
a <= b #true
"""

#boolean operators
"""
con1 = True
con2 = False

not con1 #false
con1 and con2 #false
con1 or con2 #true

#OR
print(0 or 1) #1
print(False or 'hey') #hey
print('hi' or 'hey') #hi
print([] or False) #False
print(False or []) #[]

#AND
print(0 and 1) #0
print(1 and 0) #0
print(False and 'hey') #False
print('hi' and 'hey') #hey
print([] and False) #[]
print(False and []) #False

"""

#bitwise operators
"""
& performs binary AND
| performs binary OR
^ performs a binary XOR operation
~ performs a binary NOT operation
<< shift left operation
>> shift right operation
"""

#is and in operators
"""
is #identity operator
in #membership operator
"""

#terinary operator
"""
def is_adult(age):
  if age > 18:
    return True
  else:
    return False

def is_adult2(age):
  return True if age > 18 else False
"""

#string operators
"Beau"
'Beau'
name = "Beau"
phrase = name + " is my name"
name += " is my name"
print(name)

print("""This is 

multi line 

method

""")

print("beau".upper())
print("bEaU".lower())

print(name[-1])
print(name[1:3])
print(name[:3])
print(name[1:])
print(name[:])


#strings are false when empty
#numbers are ture when not 0

#boolean
done = True
if done:
  print("yes")
else:
  print("no")

book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])
print(read_any_book)

ingredients_purchased = True
meal_cooked = False
ready_to_serve = all([ingredients_purchased, meal_cooked])
print(ready_to_serve)
