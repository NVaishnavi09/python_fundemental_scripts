month=int(input("enter the month"))
year=int(input("enter the year"))
if (month==2) & (year%4==0) and (year%100!=0) or year%400==0:
    print("29")
elif (month==2):
    print("28")
elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("31") 
else:
    print("30")     