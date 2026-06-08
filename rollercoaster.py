print("Welcome to RollerCoaster")

height = int(input("What's your height in cm? "))
age = int(input("How old are you? "))

if height >= 120:
    print("You can ride the roller coaster")

    if age < 12:
        ticket = 5
    elif age < 18:
        ticket = 7
    elif age >= 45 or age <= 55:
        print("it is safe to ride the roller coaster")
    else:
        ticket = 12

    photo = input("Do you want a photo taken? Y or N ").upper()

    total_bill = ticket

    if photo == "Y":
        total_bill += 3

    print(f"Your total bill is $ {total_bill}")

else:
    print("Sorry, you can't ride the roller coaster")
