_str=input("Enter a string: ");
_len=len(_str);
x=_str[0];
y=_str[_len-1];
z=_str.replace(x,y,1);
r=z[:_len-1]+x;
print(r);