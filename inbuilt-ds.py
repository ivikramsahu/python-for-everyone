from enum import Enum

#complex numbers

num1 = 2 + 3j
num2 = complex(2, 3)

print(num2.real, num2.imag)

#built in functions

print(abs(-5.5))
print(round(5.43, 1))

#enumarate


class State(Enum):
  INACTIVE = 0
  ACTIVE = 1


print(State['ACTIVE'].value)
print(State(1))
print(State['ACTIVE'])
print(list(State))
print(len(State))

#user input

age = "12"  #input("What is your age? ")
print("Your age is " + str(age))
print(f"Your age is {age}")  #using f with print

#control statements

condition = True
if condition:
  print("The condition")
  print("was true")
else:
  print("The condition")
  print("was false")

#lists

dogs = ["Roger", "Syd", True]

print("Roger" in dogs)
print("Beau" in dogs)
print(dogs[0])

dogs[2] = "Beau"

print(dogs[2:3])

dogs.append("rocky")
dogs.extend(["Raja", "frre"])  # += same as extends
print(dogs)

dogs.remove("Raja")
print(dogs)

dogs.pop()
print(dogs)

dogs.insert(2, "labby")
print(dogs)

dogs[1:1] = ["test1", "test2"]
print(dogs)

dogs.sort(key=str.lower)
print(dogs)
