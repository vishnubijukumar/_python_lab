_len_1=int(input("Enter the length for 1st color list : "));
_len_2=int(input("Enter the length for 2nd color list : "));
_list_1=[];
_list_2=[];
for i in (range(1,_len_1+1)):
    _list_1.append(input("Enter the "+str(i)+" th element in color list 1 : "));

for j in (range(1,_len_2+1)):
    _list_2.append(input("Enter the "+str(j)+" th element in color list 2 : "));
_diff_list=[];
for x in _list_1:
    if x not in _list_2:
        _diff_list.append(x)

print(_diff_list);


