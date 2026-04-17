print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_bill = tip / 100 * bill + bill
total_bill = bill + tip_bill
bill_per_person = tip_bill / people
final_bill = round(bill_per_person,2)
print(f"Each person has to pay {final_bill}")