dict={};
n=int(input("Enter the no of elements in dictionary:"));
for i in range(n):
	key=input("\n Enter the Key: ");
	value=input("\n Enter the Value: ");
	dict[key]=value;
r=int(input("Enter 0 for ascending and 1 for descending order: "));
s_dict=sorted(dict.items(),reverse=r);
print(s_dict);