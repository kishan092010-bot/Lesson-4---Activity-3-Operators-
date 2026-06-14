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
print("the reverse of the string is", reverse_string)