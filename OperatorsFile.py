num1=20
num2=30
num3=40
num4=50
num5=60
sum=num1+num2+num3+num4+num5
print("sum of 5 numbers is", sum)

input1=int(input("enter the first number"))
print("the first number is", input1)
input1%100
result=input1%100
print("the result is", result)



#calculate the percentage
print("enter the marks obtained in 2 subjects")

math=int(input("maths marks"))

science=int(input("science marks"))
total_marks=math+science
print("total marks is", total_marks)
percentage=total_marks/200*100
print("the percentage is", percentage, "%")

#calculate the length of the string
string=input("enter a string")
length=len(string)
print("the length of the string is", length)

#Indexing & Slicing Indexing --- get the index value and Slicing mean get the substring from string

string1="Hello World"
print(string1[0]) #H
print(string1[6:11]) #World

#String Concatenation
string2="Hello"
string3="World"
string4=string2+" "+string3
print("the concatenated string is", string4)

#Convert into Uppercase & Lowercase
string5="Hello World"
print(string5.upper()) #HELLO WORLD
print(string5.lower()) #hello world

#Program on  reverse a string
string6="Kishankumar"
reverse_string=string6[::-1]

# Identity Operators (is,is not) - used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is y) # False, because x and y are not the same object, even if they have the same content
print(x == y) # True, because both variables have the same content
print(x is z) # True
print(x is not y) # True
# Object is a real item created by Python, and it is stored in the computer memory. A variable is a name that refers to an object. When you create an object, Python automatically assigns it a unique identity (memory address). The identity of an object can be checked using the id() function.

# Memebership Operator(In, Not-In)
bag=["Book","Notebook","pencil"]
print("pencil" in bag) # True
print("laptop" in bag) # False
print("laptop" not in bag) # True

# convert 19 to binary

#19/2 ------------Quotient 9 Remainder 1

#9/2 --------------Quotient 4 Remainder 1

#4/2 --------------Quotient 2 Remainder 0

#2/2 --------------Quotient 1 Remainder 0

#1/2 --------------Quotient 0 Remainder 1

#19------------10011(bottom to top)

#16 8 4 2 1----power value (mutiply by 2)

#1 0 0 1 1

# Multiply

# 1 ×16 =16

# 0 ×8 =0

# 0 ×4 =0

# 1 ×2 =2

# 1 ×1 =1

# Add

# 16+2+1=19

# Bit-wise Operation: &, |, ^, ~, >>>, <<<
# Apply bitwise operators (AND, OR, XOR, NOT, shifts)
# Bit wise rule:(&,|)

#for and operation(&) if both bits are 1 then the result is 1 otherwise 0

#rule:

#5&3

# 101----5

#&

#011-----3

#001

#4 2 1

#0 0 1

#0+0+1=1

#or operation(|) if both bits are 0 then the result is 0 otherwise 1

#5--001

#3--011

#re-011--3

#XOR operation(^) if both bits are same then the result is 0 otherwise 1

#5--001

#3--011

#re-010--2

#left shift(<<) multiply by

#num=input("enter the number")

#num=5

#print(num<<1)moves shift to left by 1 position multiply by 2

#10

#right shift(>>) divide by

#num=8

#output4

#num7

#output

#start the code

num1=int(input("enter the first number"))

num2=int(input("enter the second number"))

print("Bitwise AND of",num1,"&",num2,"is:",num1&num2)

print("Bitwise OR of",num1,"|",num2,"is:",num1|num2)

print("Bitwise XOR of",num1,"^",num2,"is:",num1^num2)

print("Left Shift of",num1,"<< 1 is:",num1<<1)

print("Right Shift of",num1,">> 1 is:",num1>>1)

# Expressions - It's a combinations of values + variables + operators that python evaluates to produce 1 final result

# Example:
# x = 8
# y = 2
# ansvar = x * y + 4

# Operator Precedence - It means the order in which python solves operators inside an expression

# P → E → M → D → A → S/BODMAS

# P = Parentheses ()

# E = Exponent **

# M = Multiplication *

# D = Division /, //, %

# A = Addition +

# S = Subtraction -

# If two operators have the same priority (like + and -, or *, /, //, %), Python evaluates them from Left to Right.

print(10 + 2 * 3)
print((10 + 2) * 3)
print(10 - 4 + 2)

# Assignment 1

v = 4
w = 5
x = 8
y = 2
z = 0

print(int((v + w) * x/y))

# Assignment 2

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if (name == "Kishan" or name == "Isha") and age >= 15:
    print("Hello, welcome!", name)
else:
    print("Goodbye!")