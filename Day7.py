
'''
work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
        else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest streak is {longest_streak}')
#in this case when the entire loop execution is done we get result of
#else block

#same program with break 
work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(f'Longest Streak is {longest_streak}')
            break
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest streak is {longest_streak}')
print("Execution done")

#for-else with notification scenario

notifications = [0,0,0,0]
for notification in notififcations:
    if notification == 1:
        print('Unread notification')
        break
else:
    print('All caught Up')

#try  to take notification from user --> list of integers
    
notifications = list(map(int,input("Enter the value --> 0 or1:").split(',')))
print(notifications)
for notification in notifications:
    if natification == 1:
        print('Unread notification')
        break
else:
    print('All caught Up')


#while --> it relies on condition it will be completely executed untill the
#condition is satisified...

syntax while:

while <condition>:
      statement(s)...
      .........
      ........


while True:
    print("Yes")


# It runs an infinite loop we need to press ctrl + c (keyboard interrupt)

i = 0 #initialised statement
while i <=10:
    print(i)
    i=i+1 #counter

#Get the counter from 10 to 1
i = 10
while i >=1:
    print(i)
    i=i-1 # decrement i-=1

i =0
while i<=10:
    print(10-i)
    i = i+1
'''
#banking scenario --> Pin authentication if more than 3 attempts
#Account locked

pin = "2690"
max_atttempts = 3
current_attempts = 0
while current_attempt <= max_attempts:
    enter_pin = input("Enter the ATM PIN:")
    if entered_pin == pin:
        print("Login successful")
        break
    #continue #it holds for this condition and skips to the next part 
    else:
        print("Enter pin is wrong..Try again carefully")
        current_attempt +=1
    else:
       print("Account locked, try after 24hours...")
        
     
