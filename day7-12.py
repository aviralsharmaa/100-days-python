print(3+5)
print(3-5)
print(3*5)
print(3**5) #! ** ----> this is exponential multiplication
print(3/5)
print(3%5)
print(3//5) #! // ---> this is floor division operator


# ! Type Casting 
# ? Typecasting is the process of converting a value from one 
# ? data type to another. In Python, 
# ? typecasting can be done explicitly or implicitly.

#! This is explicit typecasting
a="87"
b="59"
print(int(a)+int(b));


#! This is implicit typecasting
c=5
d=3.6
print(c+d);


#! Input() function ---> it take values always as a string

e = input("Enter Your name: ")
print("My name is:",e);

f= int(input("Enter first number:"))
g= int(input("Enter second number:"))
print(f+g);

#! All About String
name="Aviral"
surname="Sharma"
gotra='Katyani'
cote='This is used for "double quotation"';

print("Hello", name);
print(cote);

#! use of multi line string

nsname = '''this is 
multi line 
string
'''
print(nsname);

print(name[0])
print(name[1])
print(name[2])
print("\n")
for character in nsname:
    print(character)


#! string Slicing
names="Aviral,sharma,suryansh,sharma"
print(names[0:6]) #! ---> get specific name through string index

print(len(names)) #! ---> get specific length of string