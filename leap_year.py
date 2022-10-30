from datetime import date
_fn_year=int(input("Enter the final year: "));
_current_date=date.today();
_current_year=_current_date.year;
_yr=[];
for i in(range(_current_year,_fn_year+1)):
    if i%4==0 or i%100==0 or i%400==0:
        _yr.append(i);
print("The List of all leap year upto "+str(_fn_year)+" is : \n",_yr);