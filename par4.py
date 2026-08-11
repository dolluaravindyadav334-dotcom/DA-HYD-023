#fibanoci series using for loop
'''
num = int(input())
a =0
b =1
for i in range(num):
    print(a,end='')
    c=a+b
    a=b
    b=c
'''
#fibanoci using while loop
num= int(input(''))
a = 0
b = 1
i = 0
while i <=num:
    print(a,end=',')
    c=a+b
    a=b
    b=c
    i=i+1
