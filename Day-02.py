#I WILL BE MAKING A TIP CALCULATOR TODAY! WHAT IT DOES IS IT TAKES THE TOTAL AMOUNT IN BILL, ASKS WHAT % YOU WANT TO GIVE AS TIP, HOW MANY PEOPLE YOU WANT TO GIVE IN CONTRI AND PRINTS THE OUTPUT
print("Welcome to the Tip Calculator\n")
bill_amount = float(input("What is the total bill?\n"))
percentage_of_tip = int(input("What percentage you want to give as tip? - 10%, 12% or 15%?\n"))
number_of_people = int(input("How many people are there including you on your table?\n"))
total = round(bill_amount + ((percentage_of_tip / 100) * bill_amount), 2)
print(f"The total bill including the tip is {total}!")
per_person = round(total/number_of_people, 2)
print(f"The per person expense is {per_person}!")