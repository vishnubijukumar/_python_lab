_first=int(input("Enter 1st number: "));
_second=int(input("Enter 2st number: "));
_third=int(input("Enter 3rd number: "));
if(_first==_second==_third):
    print("Three Number is equal")
if(_first>_second):
    if _first>_third:
        print("The biggest number is: ",_first);
    else:
        print("The biggest number is: ",_third);
elif _second>_third:
    print("The biggest number is: ",_second);
else:
    print("The biggest number is: ",_third);
