a=[]
b=[]
_operation=-1
n=int(input("size of a"))
m=int(input("Size of b"))
for i in range(1,n+1):
      c=input("Enter the element of a")
      a.append(c)
for i in range(1,m+1):
      d=input("Enter the element of b")
      b.append(d)
print("List 1:",a)
print("List 2:",b)
print("\n 1.Check whether 2 list are of same length : \n 2.Check whether 2 list are of same value : \n 3.Check whether any value occurs in both the list : \n 4.Exit")
while(_operation!=0):
 _operation=int(input("\n Enter your choice\n"))
 match _operation:
  case 1:
    if(n==m):
       print("The list are of same length\n")
    else:
       print("The list are of different length\n")
  case 2:
    a.sort()
    b.sort()
    if(a==b):
        print("The lists ae identical\n")
    else:
        print("The list are not identical\n")

  case 3:
    c=[]
    for x in a:
     for y in b:
            if(x==y):
             c.append(x)
    if(len(c)>0):       
       print("The value",c,"Occur in both list\n")
    else:
       print("No similar values occur in both lists")
  case 4:
         exit()