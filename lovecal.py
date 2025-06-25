print("The Love Calculator is calculating your score...")
name1 = input("ur name:") # What is your name?
name2 = input("ur partner name: ") # What is their name?
name_1=name1.lower()
name_2=name2.lower()
fname=name_1+name_2
t=fname.count("t")
r=fname.count("r")
u=fname.count("u")
e=fname.count("e")
fname1=t+r+u+e
l=fname.count("l")
o=fname.count("o")
v=fname.count("v")
e=fname.count("e")
fname2=l+o+v+e
score=int(str(fname1)+str(fname2))
print(score)
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif  40<score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")    