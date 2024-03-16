#banking system program

# Log in Form
print("Welcome our banking company")
name=input("Enter your name :")
confirmname=input("Enter your confirmname :")

if name=="susu" :
    print(" Open SuSu banking account ")
elif name=="mgmg":
    print("Open mgmg banking account")
else:
    print("Please try again")
for repeat in range (1,2):
    print(confirmname)

email=input("Enter your email :")
emailpassword=int(input("Enter your emailpassword :"))
confirmemailpassword=int(input("Enter your confirmemailpassword :"))
if emailpassword==confirmemailpassword :
    print("your password is correct")
else:
    print("Please check your password")
for repeat in range (1,2):
    print (confirmemailpassword)

phonenumber=input("Enter your country phonenumber :")
if phonenumber =="+959":
    print("your phone number is myanmar phone number")
elif phonenumber=="+66":
    print("Your phone number is thai phone number")
else:
    print("We have +959 and +66 so you should write this number")
for repeat in range (1,2):
        print(phonenumber)

Address=input("Enter your address :")

#Cashboard

limitamount=5000
depositamount=int(input("Enter depositamount : "))
if limitamount > 50:
    oddamount = limitamount+depositamount
    print(oddamount)
elif limitamount < 50:
    changeamount=3000
    depositamount=int(input("Enter depositamount :"))
    oddamount = changeamount+depositamount
    print(oddamount)
   
print("Thanks for banking with us!")
