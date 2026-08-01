'''
marks = int(input("Enter the marks (1-100):"))
if marks > 0 and marks <=100:
    if marks >= 90:
        print("user has secured Grade A")
    if marks >= 80:
        print("user has secured Grade B")
    if marks >= 70:
        print("user has secured Grade c")
    if marks >= 60:
        print("user has secured Grade D")
    if marks <60:
        print("user has failed,study again")
else:
     print("enter only +ve value greater than 0 and less than 100")
'''
#lif keyword --> if-elif-else
'''
if <condition1>:
   statement(s)..
   ...........
elif <condition2>:
     statement(s)..
     .........
elif <condition3>:
     statement(s)
     .........
else:
     statement(s)...
     .......


marks = int(input("Enter the marks (1-100):"))
if marks >=100:
    print("enter values should be greater than 1 and less than 100")
elif marks >= 90: and marks <100:
    print("user has secured Grade A")
elif marks >= 80: and marks <=89:
    print("user has secured Grade B")
elif marks >= 70: and marks <=79:
    print("user has secured Grade c")
elif marks >= 60: and marks <=69:
    print("user has secured Grade D")
elif marks <60: and marks >0:
    print("user has failed,study again")
else:
    print("No negative value")

#voter eligibility checkchase --> make sure to satisfy all possible conditions
#>=18  -->Access
#<18 --> no of year eligibility should tell
#negative values --> not acceptable

age = int(input("Enter the age:"))
if age>=18 and age <=100:
    print('----- User has vote Eligibility -----')
    print('----- Access Granted -----')
elif age <18 and age >0:
    print('----- user still need to get vote eligibility ----')
    print('----- user need to wait for more',(18-age),'year(s)---')
else:
    print('---- Only +ve values and less than 100 Acceptable----')


#prefer if-elif-else....

#Output --< print()
#output formatting --> old style formatting (using commas)
#% usage (%f,%f),.format() usage, fstring notation
a,b = 7,9
print(a)
print(b)
name = "Codegnan",batch = "DataAnalysis"
print(name,batch) #by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='----->')
#end ='\n',\t --->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("Hyderabad")

name="Codegnan';age=7:batch='DA-023';place='Hyderbad'
#Usage of commas
print(batch 'is in',name) #variable and msg to be separated by comma
print(name,'is in',place,'age is',age,'year')
#old style formatting --> %d -->integer, %s--> string,%f-->float
salary = 24253.256
print("His salary is %d"%(salary))
print("His salary is %f"%(salary))
print("His salary is %.1f"%(salary)) #%.if ---> rounding to 1 decimal
'''
#.format() usage
print("{} is in {}".format(name,place)) #order matter

#fstring usage (more  recommended)

print(f'{name} is in {place}')
print(f'{"Arvind"} is in {name}')
