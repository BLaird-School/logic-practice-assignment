age= int(input("Enter your age:"))
if age>= 21:
    print("You are able to buy alcohol or tabbacco products")
else:
    print("You are to young get out!")

num1= float(input("Select your first number:"))
num2= float(input("Select the second number:"))
print(f"{num1} == {num2}: {num1== num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} <= {num2}: {num1 <= num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} > {num2}: {num1 < num2}")

Test_Score= int(input("Enter Your Test Score:"))
Attendance= int(input("Enter Your Attendance Percentage:"))
if Test_Score > 70 and Attendance > 80:
    print("You pass good job!")
else:
    print("You failed try again next year")

has_state_ID= input("Do you have a state issued ID? (Yes/No):")
has_socialSecurity_card= input("Do you have a social security card? (Yes/No):")
if has_state_ID == "Yes" or has_socialSecurity_card == "Yes":
    print("You are eligable for a rental car")
else:
    print("Your denied a rental car")

your_account= input("Do you have an account with this app? (Yes/No):")
if not your_account == "Yes":
    print("You may enter the app")
else:
    print("Your banned from our app please leave or be fined $100!")

exsisting_loan= input("Do you currently have an exsisting loan with us? (Yes/No):")
credit_score= float(input("Enter credit score:"))
monthly_income= int(input("Enter your monthly income:"))
if exsisting_loan == "No" and (monthly_income >= 5000 or credit_score >= 730):
    print("You qualify for a new loan")
else:
    print("You are denied have a nice day")
git init