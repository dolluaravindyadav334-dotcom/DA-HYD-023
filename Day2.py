<<<<<<< HEAD
'''
Token --> vairables,Punctuators

variables --> named memory location its a placeholder for data
#rules are to be followed
'''
#multiAssignment of variables

name,age,place='codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='------>')

#a,b=2,4,5 #valueerror as too many value to unpack
#Reassigning variables

name ="codegnan"
a,b =34,1.5
print(a,b)
a,b = b,a #swaping
print(a,b,sep=',')

#a,b = b,c #NameError as c is not defined
#print(a.b)

#Deleting the variables -->del
#del a
#print(a)
del a,b
print(a,b)

#Punctuators --> [](lists),()(tuple),{}(Dict,sets)
name = "codegnan";age = 7;course ='Data_Analysis'
print(name,age,course)
'''
#datatype --> Numeric (int,float,complex),boolean,none,
            #-->sequences -->Lists,Tuples,sets,strings,
                 #          frozensets,mappings(dict)
                 
#Numeric type -->int,float,complex

#int datatype --> quantity,age..
age=7
print(age)
print(type(age)) #type --> return the datatype of object

print(type(235))
'''
'''
#quantity = 03 #it is not allowed
#print(quantity)

#float datatype --> temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))

#complex -->combination of real and imag
i2 = 4
data= 5 + i2
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))

#Boolean --> True / False

valid= True
print(type(valid))

error= False
print(type(error))
'''
'''
age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age) #return True for existing data
print(d)
e = bool(0)
print(e)
'''
#Float --> Typecasting --> int,comple,bool
'''
price = 750.56
print(type(price))
d=  int(price)
print(d)
print(type(d))
e = complex(price)
print(e)
print(type(e)) 
f = bool(price)
print(f)
'''
''''
#complex -->Typecasting --> int, float,bool
data = 2+5j
print(type(data))
#b = int(data) #TypeError
#print(C)
d = bool(data)
print(d)
print(type(d))


d = 5+4.5
print(d)


e = int(float(bool(45)))

print(e)

'''   
f = 45 + 2.5 + 2 + 3j + False
print(f)
=======
'''
Token --> vairables,Punctuators

variables --> named memory location its a placeholder for data
#rules are to be followed
'''
#multiAssignment of variables

name,age,place='codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='------>')

#a,b=2,4,5 #valueerror as too many value to unpack
#Reassigning variables

name ="codegnan"
a,b =34,1.5
print(a,b)
a,b = b,a #swaping
print(a,b,sep=',')

#a,b = b,c #NameError as c is not defined
#print(a.b)

#Deleting the variables -->del
#del a
#print(a)
del a,b
print(a,b)

#Punctuators --> [](lists),()(tuple),{}(Dict,sets)
name = "codegnan";age = 7;course ='Data_Analysis'
print(name,age,course)
'''
#datatype --> Numeric (int,float,complex),boolean,none,
            #-->sequences -->Lists,Tuples,sets,strings,
                 #          frozensets,mappings(dict)
                 
#Numeric type -->int,float,complex

#int datatype --> quantity,age..
age=7
print(age)
print(type(age)) #type --> return the datatype of object

print(type(235))
'''
'''
#quantity = 03 #it is not allowed
#print(quantity)

#float datatype --> temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))

#complex -->combination of real and imag
i2 = 4
data= 5 + i2
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))

#Boolean --> True / False

valid= True
print(type(valid))

error= False
print(type(error))
'''
'''
age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age) #return True for existing data
print(d)
e = bool(0)
print(e)
'''
#Float --> Typecasting --> int,comple,bool
'''
price = 750.56
print(type(price))
d=  int(price)
print(d)
print(type(d))
e = complex(price)
print(e)
print(type(e)) 
f = bool(price)
print(f)
'''
''''
#complex -->Typecasting --> int, float,bool
data = 2+5j
print(type(data))
#b = int(data) #TypeError
#print(C)
d = bool(data)
print(d)
print(type(d))


d = 5+4.5
print(d)


e = int(float(bool(45)))

print(e)

'''   
f = 45 + 2.5 + 2 + 3j + False
print(f)
>>>>>>> 692a45d6f05000914f140396e0e162d25de3e1a5
