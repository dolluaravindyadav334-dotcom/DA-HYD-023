'''
marks = []
for i in range(3):
    mark = int(input("Enter the marks: "))
    marks.append(mark)
marks.insert(0, 90)
marks.extend([75, 85])
print(marks)
if 75 in marks:
    marks.remove(75)
    print('remove the 75',marks)
removed = marks.pop()
print("Removed value:", removed)
print("Final list:", marks)
print("Length:", len(marks))



numbers = [20, 10, 30, 20, 40, 20] 
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
num=int(input('enter the number:'))
if num in numbers:
    print('count:',numbers.count(num))
    print('index:',numbers.index(num))
else:
    print('Number is not found')
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#3

numbers = [10, 15, 20, 25, 30, 35]
even = []
odd = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even:", even)
print("Odd:", odd)
print('Slicing first 3 digits:',numbers[:3])
print('Slicing last 3 digits:',numbers[3:])
copy_numbers = numbers.copy()
print("Copy:", copy_numbers)

numbers.clear()
print("After clear:", numbers)

#4)

names=['Asha','Rahul','Asha','John','Rahul']
name=set(names)
print(name)
name.add('Meera')
print('Adding:',name)
name.update(['Arun','Priya'])
print('Updating:',name)
if 'John' in name:
    name.remove('John')
    print('Removing',name)
name.discard('David')
print(name)
print('Unique Name:')
for i in name:
    #print('--------Unique Names-------')
    print(i)
   ''' 
#5)

python_students = {"Asha", "Rahul", "John", "naveen"}
da_students = {"Rahul", "naveen", "Arun"} 
students=python_students.union(da_students)
print('Union:',students)
common=python_students.intersection(da_students)
print('Intersection:',common)
learning=python_students-da_students
print('Only Python:',learning)
course=da_students^python_students
print('Learning only one course Data analytcs:',course)
if da_students.issubset(python_students):
    print('DA students are a subset of Python students')
else:
    print('DA students are NOT a subset of Python students')
if python_students.issuperset(da_students):
    print('Python_students are a superset of Da students')
else:
    print('Python students are NOT a superset of Da students')
if python_students.isdisjoint(da_students):
    print('Python students are  a disjoint of Da students')
else:
    print('Python students are not a disjoint of Da students')

