_len=int(input("Enter the length for the list : "));
_list=[];
_list_positive=[];
for i in (range(1,_len+1)):
    _list.append(int(input("Enter the "+str(i)+" th element in list 1 : ")));

##for i in _list:
##	if i>0:
##		_list_positive.append(i);
_list_positive=[x for x in _list if x>0]
print(_list_positive)
	

