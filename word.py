_wrd=input("Enter the Word: ");
_wrdlist=_wrd.split();
# _wordlist=list(set(_wrdlist));
_occurence_str='';
for x in _wrdlist:
    _occ=0;
    for y in _wrdlist:
        if x==y:
            _occ+=1;
    _occurence_str+="Word: '"+str(x)+"' occurrence: "+str(_occ)+"\n";
print(_occurence_str)
