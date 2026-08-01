'''
identity operators -->check the identity of an object --> id()

a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5)

a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#As we have  lists (mutable collection) both c and a lists will have different
#ids whereas values are same
print(c is a) #output  false
print(c == a) #output True
print(a is not c)


#Bitwise operators --> we perform bitwise operations over operands
#& (and) , | (or),^(XOR),shifting operators (<<,>>)

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3) #bitwise OR

print(5^3) #bitwise XOR

print(5 and 3) #here and is logical operators checks for both existances
#returns 5 in above case
print(5 or 3) #returns 3 in this case

#leftshift operator << ,Right shift Operator >>

print(5 < 1) #false comparsion
print(5 << 1) #left shift operation by position
print(5 >> 1) #Right shift operation

print(15 << 2)  #covert 15 to binary and perform 2 time left shifting

print(15 >> 2) #same 2 time right shifting



#Input formatting --> input(),int(input()),float(input())
# you  know --> single input
#2 or 3 input --. map()
# group of integer --> list(map(int,input().split(','))

name - input("Enter the name:").split(',')
print(names)

name1,name2 = map(str,input("Enter the friends names:"),split(','))
print(name1,name2)
'''
#Token --> Numeric Datatypes --> operators --> flow of the  program
#control Block statement
#conditional statement --> if,else,elif(rely on condition to the executed
#Repetition statement (loop) --> for,while

#conditional statement -->if usage
'''
syntax :
if <condition>:
    statement(s)...
    .....


age = 15
age = int(input("Enter the age:"))
if age >18:
    print('your age is:',age)


age = int(input("Enter the age:"))
if age>=18 and age in [19,21,20]:
    print('your age is',age)
print(age)

#else keyword --> if-else
else:
    statement(s)..

if-else usage as below:

if <condition>:
    statement(s)...
    ...
else:
    statement(s)....
    ...

#vote elibility  -->To check his/her voter eligibilty and give access...

age = int(input("enter the age:"))
if age>=18:
    print"you have voter eligibity and age is",age)
    print("Access Granted")
else:
    age = 18-age
   # print("you dont have eligibility as your is"'age,"year)
   print("you need to wait for more",age,"years")
   
#same case let's use only nested --> if,else
if age >0:
   if age>=18:
    print"you have voter eligibity and age is",age)
    print("Access Granted")
else:
    age = 18-age
   # print("you dont have eligibility as your is"'age,"year)
   print("you need to wait for more",age,"years")
else:
    print("you have entered -ve value/zero enter only +ve")


task : student marks and grade analayer
'''
marks=int(input("Enter a marks:"))
if marks>=90: 
    print("The grade is A",marks)
if marks>=80 and marks<90:
    print("The grade is B",marks)
if marks>=70 and marks<80:
    print("The grade is c",marks)
if marks>=60 and marks<70:
    print("The grade is D",marks)
if marks < 60:
    print("The grade is fail")
else
    
