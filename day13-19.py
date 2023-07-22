 #! String Method in python 
 #! Strings are immutable

name="aviral !!#@ okay 12.32"
print(len(name))
print(name.upper())
print(name.lower())
print(name)
print(name.rstrip("!#@"))
print(name.replace("Aviral!!#@", "Aviral Sharma 1 43 12.3"))
print(name.split(" "))

name2="i am learning pythON 100 dAys"
print(name2.capitalize()) 
print(name.capitalize()) 


print(name.center(50))

print(name.count("a"))


# ! if-else statement

a = int(input("Enter your age: "))
print("Your age is:",a)

if (a>18):
  print("You can drive")
else:
  print("Yo can not drive")

#! Conditional Operator
#? < > <= >= == = !=

print(a==18)
print(a>=18)
print(a<=18)
print(a<18)
print(a>18)
print(a!=18)