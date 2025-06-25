size=input("size of the pizaa S,M,L")
peproni=input("do you want peproni Y or N")
chesee=input("do you want cheese Y or N")
if size=='S':
    bill=15
elif size=='M':
    bill=20
else:
    bill=25

if peproni=='y' :
  if size=='S':
    bill=bill+2
else:
    bill=bill+3
if chesee=='Y':
    bill=bill+1
print(f"your pizza cost is${bill}")    
     

