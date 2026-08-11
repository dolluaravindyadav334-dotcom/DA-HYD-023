'''
String --> Caseconversions, serching & finding,string testing methods
Replace,Space removal

#searching,finding,replacing, joining
a = "codegnan"
print(len(a))
print(min(a))
print(max(a))

b = a.index('g') #it returns the index position
print(b)
c = a.index('n') #it returns only the first occurance
print(c)
d = a.index('n',6) #it returns the next occurance
print(d)
#e = a.index('n',8) #value error
#print(E)
#f = a.index('t') #valueerror
#print(F)
g = a.index('n',1,4)

#rindex() --> returns last occurance
b = a.rindex('g')
print(b)
c = a.rindex('n') #here 'n' occuring at 7th index
print(c)
#d = a.rindex('n',8) #it returns valueError
#print(d)

#count() -->returns the number of items object is repeating

print('codegnan'.count(n))
print('code'.count(w)) #it return 0 as we dont 'w' in 'code'
print('Dolluaravind'.count('a'))

#find() --> first occurance but it avoid error return -1 if subtring is
#not found
print('codegnan'.find('r')) #it returns -1

print('codegnan'.find('n'))

print('codegnan'.rfind('n'))

a = "Dolluaravind"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))
    

#replace,splitting,joining

#strings are Immutable
a = 'codegnan'
#a[4]= 's'
print(a.replace('g','s'))
print(a)
a = a.replace('g','s')
print(a)
print('uduycggw#bciwihe'a.replace('#,''))
print(a.replace('x','aravind'))

a = 'code Aravind python'
print(len(a))
b = a.split() #by default if we have space it split
print(b)
print(len(b))
c = 'code,Aravind,python'
d= c.split()
print(d)
e = c.split(',')
print(e)

#join()

a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('Aravind'))
print(a+b)
print(' '.join('Aravind'))

#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()....

a = 'Aravind123'
print(a.isalnum())
b = 'Aravind'
print(b.isalnum())
print(a.isalpha())  #return true only for alphabests
print(a.isdigit()) #return true only for digit string
print('9666736509'.isdigit())
print('2345'.isnumeric()) #this has upper edge (numbers,fraction,romans
print('Aravind'.startswith('A'))
print('Aravind'.startswith('v',4))
print('Aravind'.endswith('d'))

print('codegnan'.islower()) #return true  for all lowercase
print('COdegnan'.isupper())
print('Codegnan python'.istitle())


# space removal ---> strip() (removes leading and trailing spaces)
a='codegnan'
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print('123'.zfill(4))
print('123'.zfill(7))
#center(),ljust(),rjust()--> alignment of string check length and then modify the width accodingly
print('hai'.central(6))
print('hai'.central(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))
