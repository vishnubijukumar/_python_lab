class rectangle:
    length=0;
    breadth=0;
    def area(self):
        return self.length*self.breadth;
    def perimeter(self):
        return 2*(self.length+self.breadth);
    def compareArea(self,rectObj):
        if(self.area()>rectObj.area()):
            print("Area of 1st rectangle is greatest with area= ",self.area());
        else:
            print("Area of 2nd rectangle is greatest with area= ",rectObj.area());
r1=rectangle();
r1.length=int(input("Enter 1st rectangle's length: "));
r1.breadth=int(input("Enter 1st rectangle's breadth: "));
print("Area of the 1st Rectangle= ",r1.area());
print("Perimeter of the 1st Rectangle= ",r1.perimeter());
r2=rectangle();
r2.length=int(input("Enter 2nd rectangle's length: "));
r2.breadth=int(input("Enter 2nd rectangle's breadth: "));
print("Area of the 2nd Rectangle= ",r2.area());
print("perimeter of the 2nd Rectangle= ",r2.perimeter())
r1.compareArea(r2);