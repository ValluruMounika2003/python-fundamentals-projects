print("Welcome to the tip Calculator")
total_bill=float(input("What is your total bill ? $ "))
tip = int(input("how much tip would you like to give 10,12 or 15!"))
tip = tip / 100
total_with_tip=(total_bill * tip)+total_bill
split = int(input("How much do you want to split the tip ? "))
print(round(total_with_tip / split,2))