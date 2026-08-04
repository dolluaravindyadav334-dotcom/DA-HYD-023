'''
age = int(input("Enter your age"))
if age >= 18:
          print("your have vote eligibility")
else:
  age <18
  print("your  not eligibile for vote")
  

num = int(input("Enter a number"))
if num == 0:
    print("zero is neither even or odd")
elif num <0:
    if num %2==0:
        print("-ve even number")
    else:
            print("-ve odd number")
else:
    if num%2==0:
        print("Even number")
    else:
            print("odd number")
    

marks = int(input("enter the marks"))
if marks >100:
    print("invalid marks entered")
elif marks>=90:
    print(" Grade A")
    print(" Remark outstanding")
elif marks>=80 and marks <=89:
    print(" Grade b")
    print(" Remark Excellent")
elif marks>=70 and marks <=79:
    print(" Grade c")
    print(" Remark Good")
elif marks >=60 and marks <=69:
    print("Grade D")
    print(" Remark fair")
elif marks >=50 and marks <=59:
    print("Grade E")
    print("Remark poor")
else:
    print("Grade F")
    print("fail")
'''
temp = int(input("Enter the month number"))
if temp >12:
    print("invalid month entered")
elif temp==12 or temp==1 or temp==2:
    print("winter")
elif temp==3 or temp==4 or temp==5:
    print("spring")
elif temp==6 or temp==7 or temp==8:
    print("summer")
else:
    print("Autumn ")
    

    
