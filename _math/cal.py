print("welcome to the tip calculator")
bill = float(input("enter the total bill:"))
tip = int(input("enter the tip of the bill"))
people = int(input("enter no.of people"))
bill_percent = tip / 100
total_bill = bill_percent * bill
total_amount = total_bill + bill
total_bill_amount=total_amount/people
#print(total_bill_amount)
total=round(2,total_bill_amount)
print(total)
