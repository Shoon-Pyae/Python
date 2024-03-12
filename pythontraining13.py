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

email=input("Enter your email :")
emailpassword=int(input("Enter your emailpassword :"))
confirmemailpassword=int(input("Enter your confirmemailpassword"))
if emailpassword==confirmemailpassword :
    print("your password is correct")
else:
    print("Please check your password")

phonenumber=input("Enter your country phonenumber :")
if phonenumber =="+959":
    print("your phone number is myanmar phone number")
elif phonenumber=="+66":
    print("Your phone number is thai phone number")
else:
    print("We have +959 and +66 so you should write this number")

Address=input("Enter your address :")

# Dashboard
susucurrentamount=print("susu current amount",50000)
susudepositamount=int(input("Enter depositamount : "))
if susucurrentamount > 50:
    susuoddamount = susucurrentamount+susudepositamount
    print(susuoddamount)
elif susucurrentamount < 50:
    susuwithdrawlamount=int(input("Enter withdrawl amount : "))
    susuwithdrawlamount= susucurrentamount-susuwithdrawlamount
    print(susuwithdrawlamount)

mgmgcurrentamount=print("mgmg current amount",10000)
mgmgdepositamount=int(input("Enter depositamount :"))
if mgmgcurrentamount > 10:
    mgmgoddamount=mgmgcurrentamount+mgmgdepositamount
    print(mgmgoddamount)
elif mgmgcurrentamount < 10:
    mgmgwithdrawamount=int(input("Enter mgmgwithdrawamount :"))
    mgmgwithdrawamount=mgmgcurrentamount-mgmgwithdrawamount
    print(mgmgwithdrawamount)

print("Thanks for banking with us!")
