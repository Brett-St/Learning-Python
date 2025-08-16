print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill?\n£"))
tip = int(input("Would % would you like to tip?\n"))
people = int(input("How many people are splitting the bill?\n"))

bill_with_tip = tip / 100 * bill + bill
split_bill = bill_with_tip / people
round(split_bill, 2)

print(f"Each person should pay: £{split_bill}" )