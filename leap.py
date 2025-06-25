year = int(input())
# 🚨 Don't change the code above 👆
if (year%4==0&year%100!=0):
        print("Leap year")
elif (year%4==0&year%100==0&year%400==0):
 print("Leap year")
elif (year%4==0&year%100!=0&year%400!=0):
  print("Not a leap year")
else:
  print("Not leap year")