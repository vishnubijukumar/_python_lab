_len_1=int(input("Enter the length for the list : "));
_list=[];
_list_2=[];
for i in (range(1,_len_1+1)):
    _list.append(input("Enter the "+str(i)+" th element : "));

for x in _list:
    _list_2.append(ord(x));

print("The ordinal values are: ",_list_2);