_ls=input("Enter the numbers : ");
_list=_ls.split();
print(_list);
_sqlis=[int(x)*int(x) for x in _list];
#for x in _list:
#	_sqlis.append(int(x)*int(x));
print(_sqlis);
