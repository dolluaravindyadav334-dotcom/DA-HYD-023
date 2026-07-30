#Numeric data type  --> int, float,complex along with boolean

#Input formatting -->Accepting input from the user --> input()

#Accepting integer input from user
#by default input() accepts any input --> str
#int(input()) --> will accept only integers
'''age = int(input('Enter the age'))
print(age)
print(type(age))
      
age = float(input('Enter the age'))
print(age)
print(type(age))

#Accepting string input from user

name = input("Enter the name:")
print(name)
print(type(name))'''
'''
#Accept group of values

a = input().split() #by default split() has space
print(a)

#space separated values
a = input().split() #now you enter spaces in output
print(a)

#comma separated values
a = input("Enter the value:").split(',')
print(a)

#list of integers
marks = list(map(int,input("Enter the value:").split(',')))
print(marks)

#now we want to accept 2 value from user
age,salary = map(int,input("Enter the value:").split(','))
print(age)
print(salary)

#single input --. int(input())
#two inputs -->a,b = map(int,input().split(','))
#any number result as list --> a = list(map(int,input().split(',')))


#float of integers
marks = list(map(float,input("Enter the value:").split(',')))
print(marks)

#group of float values
age,salary = map(int,input("Enter the value:").split(','))
print(age)
print(salary)


#Accepting input from user --> int,float -->input formatting

#operators --> Operators perform operations between value (operands)
#7 type --> Arithmetic,Assignment,camparsion (Relationship)
#membership,Identity,logical,bitwise

#Arithmetic operators -->Arihmetic operators
#+ , - ,*,/
print(5+2)
print(7-8)
print(3*8)
print(4/9) #float value
#Floor Division (Integer division) -->returns quotient
print(4//9)
#modulus -->division rules --> return  remainder
print(5%3)
#power


l= int(input("enter the length"))
b= int(input("enter the breadth"))
area= l*b
print(area)

#Assignment operators --> asign the values
# = , += , -=
a = 45
print(a)
#update the value of a
a = a + 5 #a+=5
print(a)
#update the value of a
a = a + 5 #a+=5
print(a)
b = 35
b += a #b = b + a
print(b)
b -= 5 #b = b-5
print(b)

#Task : *=,/=,//=,**= workout

#comparsion operators -->we compare the value -->boolean
# == (equal to ), != (not equal to ), < (less than) , >(greater than)
# <=(less than or equal to) >= (greater than or equal to)

age = 25
print(age == 25) #returns boolean output
print(age != 35)
print(age < 25)
print(age <=25)
print(age >35)
print(age >= 35)

print(-5 < -1)

#membership operators --> in,not in -->boolean
#it check for existance of an object in a collection

marks = [56,75,45,85]
print(34 in marks)
#print(34 in 255) #TypeError

print(34 not in marks)
print('code' in 'codegnan')
print('$' in 'abc$frg')


#logical operator --> logical decision making -->and,or,not
#and -->all condition to be satified
#or --> any one condition be satified

a = (25 in [25,45,65]) and 45 < 56
print(a)
b = 45 > 56 or 25 <=45
print(b)
c = not(True)
print(C)
'''
#Indentity operators --> check for identify of an object --> id()
#is ,is not
a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)

      

