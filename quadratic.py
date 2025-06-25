import math
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
#these are the coefficients of the quadratic eq
if a==0:
    print("a cant be zero")
elif a>0:
    d=b*b-4*a*c
    print("d: ",d)
    root=math.sqrt(abs(d))
    if d>0:
        print("the roots are unique and real")
        print((-b+root/2*a))
        print((-b-root/2*a))
    elif d==0:
        print("the roots are equal")
        print((-b/2*a))
    else:
        print("the roots are imaginary")
        print((-b/2*a,'+i',root))
        print((-b/2*a,'-i',root))
else:
    print("give crct values")
