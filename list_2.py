a=list(map(int,input("\n Ente the list1\n")))
b=list(map(int,input("\nEnter the list2\n")))
print("List 1:",a)
print("List 2:",b)
print("\n 1.Check whether 2 list are of same length : \n 2.Check whether 2 list are of same value : \n 3.Check whether any value occurs in both the list : \n 4.Exit")
if(len(a)==len(b)):
     print("The list are of same length\n")
else:
      print("The list are of different length\n")
   
if(sum(a)==sum(b)):
        print("The lists ae same sum\n")
else:
        print("The list are not same sum\n")
c=[]
for x in a:
     for y in b:
            if(x==y):
             c.append(x)
if(len(c)>0):       
       print("The value",c,"Occur in both list\n")
else:
       print("No similar values occur in both lists")