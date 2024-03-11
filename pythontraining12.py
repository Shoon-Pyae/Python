# library booking system

shopname=input("Enter your shopname :")
name=input("Enter your name :")
confirmname=input("Enter your confirmname :")

if name==confirmname:
    print("Welcome library ")
else:
    print("Try again")

startdate=input("Enter your start date ")
returndate=input("Enter your return date :")
dateofbirth=input("Enter your date of birth :")
email=input("Enter your email :")
confirmemail=input("Enter your confirmemail :")

if email==confirmemail:
    print("successful")
else:
    print("incorrect, Please check it again :")
address=input("Enter your address :")
phonenumber=input("Enter your country number:")
if "+959" == phonenumber:
    print("your phone number is myanmar phone number")
elif "+91" == phonenumber:
    print("Your phone number is thai phone number")
else:
    print("We have +959 and +91 so you should write this number") 

gender=input("Enter your gender :")
nameofbook=input("Enter your name of book :")
booktitle=input("Enter your book title :")




