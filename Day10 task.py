<<<<<<< HEAD
'''
b=4,6,1,0,2,4,0,6
runs=list(map(int,input().split()))
total_score=boundaries=dotballs=0
for i in runs:
    total_score+=i
    if i==4 or i==6:
        boundaries==1
    elif i==0:
        dotballs+=1
        print("total_score",total_score)
        print("boundaries",bondaries)
        print("dotballs",dotballs)

pin=4534
max_attempts=3
current_attempts=0
while current_atttempt<=max_attempts:
    entered_pin=input("Enter the ATM pin:")
    if entered_pin ==pin:
        print("login_successful")
        break
    else:
        print("enter PIN is wrong..Try again carefully")
        current_attempt+=1
    else:
        print("Account locked,try after 24hours..")

'''
pin=4534
max_attempts=5
current_attempts=0
while current_atttempt<=max_attempts:
    entered_pin=input("Enter the ATM pin:")
    if entered_pin ==pin:
        print("login_successful")
        break
    else:
        print("enter PIN is wrong..Try again carefully")
        current_attempt+=1
    else:
        print("Account locked,try after 24hours..")

=======
'''
b=4,6,1,0,2,4,0,6
runs=list(map(int,input().split()))
total_score=boundaries=dotballs=0
for i in runs:
    total_score+=i
    if i==4 or i==6:
        boundaries==1
    elif i==0:
        dotballs+=1
        print("total_score",total_score)
        print("boundaries",bondaries)
        print("dotballs",dotballs)

pin=4534
max_attempts=3
current_attempts=0
while current_atttempt<=max_attempts:
    entered_pin=input("Enter the ATM pin:")
    if entered_pin ==pin:
        print("login_successful")
        break
    else:
        print("enter PIN is wrong..Try again carefully")
        current_attempt+=1
    else:
        print("Account locked,try after 24hours..")

'''
pin=4534
max_attempts=5
current_attempts=0
while current_atttempt<=max_attempts:
    entered_pin=input("Enter the ATM pin:")
    if entered_pin ==pin:
        print("login_successful")
        break
    else:
        print("enter PIN is wrong..Try again carefully")
        current_attempt+=1
    else:
        print("Account locked,try after 24hours..")

>>>>>>> 43560a0 (Add Day 10 task and par4, update day8)
