_len_1=int(input("Enter the length for the list : "));
_list=[];
_list_2=[];
for i in (range(1,_len_1+1)):
    _list.append(input("Enter the "+str(i)+" th element : "));

for x in _list:
    if int(x)>100:
        _list_2.append(x);

print(_list_2);