a=int(input("enter the a: "))
b=int(input("enter b: "))
i=max(a,b)
for x in range(i,a*b):
    if x%a==0 and x%b==0:
        lcm=i
        break
print(lcm)  