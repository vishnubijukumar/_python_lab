# list 
_len_1=int(input("Enter the length for 1st list : "));
_len_2=int(input("Enter the length for 2nd list : "));
_list_1=[];
_list_2=[];
for i in (range(1,_len_1+1)):
    _list_1.append(input("Enter the "+str(i)+" th element in list 1 : "));

for j in (range(1,_len_2+1)):
    _list_2.append(input("Enter the "+str(j)+" th element in list 2 : "));

# print(_list_2,_list_1);
flag=1;
while flag:

    _operation=int(input("Select Operation: \n 1.Check whether 2 list are of same length : \n 2.Check whether 2 list are of same value : \n 3.Check whether any value occurs in both the list : \n"));
    # print(_operation);
    match _operation:
        case 1:
            if _len_1==_len_2:
                print("The 2 list are of same length ");
            else:
                print("The 2 list are not the same length ");
        case 2:
            _list_1.sort();
            _list_2.sort()
            if _list_1==_list_2:
                print("The list are identical");
            else:
                print("The list are not identical");
        case 3:
            _identical_items=[];
            for x in _list_1:
                for y in _list_2:
                    if x==y:
                        _identical_items.append(y);
            if len(_identical_items)>0:
                print("There are common elements : ",_identical_items);
            else:
                print("There are no common elements ");
    flag=int(input("Do you want to continue enter 1 for yes and 0 for no : "));
    if flag>1:
        flag=0;
        




