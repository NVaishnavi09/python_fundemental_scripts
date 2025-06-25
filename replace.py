num=int(input("enter the num: "))
new=[]
numstr=str(num)
print(numstr)
for i in numstr:
    if(i=='0'):
        new.append('1')
    else:
        new.append(i)
newnum=""
for i in new:
    newnum+=i
print(int(newnum))                