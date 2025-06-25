import random

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=['@','#','$','%','^','&','*','(',')','!']
num=['1','2','3','4','5','6','7','8','9','0']

l=int(input("enter no of letter: "))
s=int(input("enter no of symbols: "))
n=int(input("enter no of numbers: "))
password =[]
for char in range(1,l+1):
    password.append(random.choice(letters))
for char in range(1,s+1):  
    password+=random.choice(symbols)
for char in range(1,n+1):
    password+=random.choice(num)
#print("your password is",random.choice(password))
random.shuffle(password)
#print(password)
pas=""
for char in password:
    pas+=char
print(f'your password is: {pas}')    