print("Welcome to Tip calculator!")
bill = float(input("What is the total bill ? "))
tip = int(input("Tip you want to pay ? $10,12 or 15 "))
person= int(input("How many people to split ? "))
total_tip = bill * (tip/100)
total_bill = bill+ total_tip
per_person= total_bill/person
final = round(per_person, 2)
print(f"each person should pay : ${final}")
