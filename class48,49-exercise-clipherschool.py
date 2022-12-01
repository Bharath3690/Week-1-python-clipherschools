user_name=input("enter your name:")
user_age=input("enter your age:")
user_age=int(user_age)
if user_age >=10 and (user_name[0]=='a' or user_name[0]=='A'):
    print("you can watch movie")
else:
    print("you cannot watch movie")