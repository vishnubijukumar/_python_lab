_str=input("Enter a sentence: ");
x=_str.replace(_str[0],'$');
x=x.replace('$',_str[0],1);
print(x);