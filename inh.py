class publisher:
    pubName="";
    pubAddress="";
    def __init__(self):
        self.pubName="DC";
        self.pubAddress="ABC villa";
    def addDetails(self):
        print("Inside publisher");
        self.pubName=input("Enter the Publisher Name: ");
        self.pubAddress=input("Enter the Publisher Address: ");
    # def addDetails(self,pname,paddress):
    #     self.pubName=pname;
    #     self.pubAddress=paddress;       

class book(publisher):
    bookName="";
    bookAuthor="";
    def __init__(self):
        self.bookName=input("Enter the book Name: ");
        self.bookAuthor=input("Enter the Author Name: ");
        

class pythonBook(book):
    price="";
    no_of_pages="";
    def __init__(self):
        self.price=input("Enter the book price: ");
        self.no_of_pages=input("Enter the no_of_pages: ");
        super().__init__();
    def addDetails(self):
        print("Inside pythonBook");
        self.pubName=input("Enter the Publisher Name: ");
        self.pubAddress=input("Enter the Publisher Address: ");    
    def display(self):
        print("Book Details: ");
        print("Book Name: ",self.bookName);
        print("Book Author: ",self.bookAuthor);
        print("Publisher Name: ",self.pubName);
        print("Publisher Address: ",self.pubAddress);
        print("Book Price: ",self.price);
        print("No of Pages: ",self.no_of_pages);

b=pythonBook();
b.addDetails();
# b.addDetails("Marvel","STanLee Villa");
# b.addbookDetails();
b.display();