_num=int(input("Enter the number: "));
_factorial=1;
if _num<0:
    print("The factorial is undefined ");
elif _num==0:
    print("The factorial of ",_num," is: ",_factorial);
else:
    for i in(range(1,_num+1)):
        _factorial*=i;
    print("The factorial of ",_num," is: ",_factorial);