_len_1=int(input("Enter the length for the list : "));
_list=[];
# _list_2=[];
for i in (range(1,_len_1+1)):
    _list.append(input("Enter the "+str(i)+" th name : "));
_acnt=0;
for x in _list:
    cn=x.count('a')
    if(cn):
        _acnt+=cn;
print("The no of times 'a' occured within the list is : ",_acnt);
