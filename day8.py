   
#sequence --> strings,lists,sets,tuples,mapping(dict)

#strings -->group of characters,we use single or double or triple quotes
#for representation of strings..
#strings are Immutable,ordered, indexed collection
#space is also a character

name = 'codegnan'
'''print(name)
print(type(name))
print(len(name)) #len -->return the number of items in containers

#index() -->fetch the object (position)start at 0 and end at len (obj)
#we use [] representation
print(name[0])
print(name[5])
#print(name[25]) #IndexError --> as its out of range

#Negative Indexing --> -1 to len(obj)
print(name[-1]) #it returns last character
print(name[-3])
#print(name[-33]) #indexError

#slicing --> we can access group of characters(objects)
#we use [start:end] #start default --> 0,start is included,end is excluded

print(name[:])  #return entire string
print(name[0:]) #return entire string
print(name[:4]) #start at 0th index before 4th index
print(name[1:5])
'''

name='Python'
'''print(name[7:3])
print(name[7:3]) #return empty as string are immutable 
#slicing is applicable from lower index to higher index
print(name[:45]) #return till end of the string
print(name[45:])

print(name[-1:-5]) #return empty string
print(name[-5:-1]) #start at -5 and ends at -2
#print 'on' from above string
print(name[4:])
print(name[4:6])
print(name[-2:])

print(name[1:-2])
print(name[2:-6])
#observe +ve, +ve,-ve-ve & +ve,-ve all possibilities


#Striding -->[start:End:step]

course ='DataAnalysis'
print(len(course))
#Data -->result
print(course[:4])
print(course[4:])
print(course[-3:])

print(course[::1]) #return all characters
print(course[::2]) #includes start to end skipping charaters

print(course[1:6:3]) #[1:6] -->ataAn -->[1:6:3} --> aA
print(course[2::3])#tnys

print(course[::-1]) #it return the reverse of a string

print(course[::-2])


#task: workout with all possibilities of slicing and striding on a example

name = 'codegnan'
#Operations on string -->Indexing concatenation,repetition
print(name * 3)
print('*' * 25) #repetition

#concatenation ->combining strings

data='Arvind'+'python'+' '+'database'
print(data)
print('123'*4) #numeric string
print('code' in 'codegnan')


for i in 'codegnan':
    print(i,end=' ')
    
name = "maskmelon"
#built-in function-->len(),min(),max(),sorted()
print(len(name))
print(min(name)) #alphabetical order ASCII ordering
print(ord('M'))
print(ord('m'))
print(chr(97))
print(max(name))
print(sorted(name)) #return a list by sorting all elements
'''
#Method on string --> case - conversions,finding/searching...
name = 'watermelon'
#case-conversions --> upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
b = name.lower()
print(b)
#capitalize() --> coverts first letter to upppercase
c = name.capitalize()
print(c)
d = name.title()#coverts every word first letter to uppercase
print(d)

#Task : A to Z
# use loops and string to return A-Z
