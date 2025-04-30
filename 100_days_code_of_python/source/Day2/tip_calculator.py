

print("Welcome to the tip calculator!")

#total_bill
total_bill = float(input("What was the total bill? $"))

#tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

#people
people = int(input("How many people to split the bill? "))

final_amount = round((total_bill + ((total_bill/100)*tip))/people, 2)

print(f"Each person should pay: ${final_amount}")