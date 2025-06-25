name=input("enter the name: ")
roll=int(input("enter the roll no: "))
lst=[]
n=int(input("enter the no of  subjects: "))
for i in range(0,n):
  x=int(input('marks: '))
  lst.append(x)
  
print(lst)
marks=0
sum=n*100
for i in lst:
    marks=marks+i
print("sumof the subjects",marks)
average=marks/n
print('average:',average)
percent=(marks/sum)*100  
print("percentage of the student: ",percent)