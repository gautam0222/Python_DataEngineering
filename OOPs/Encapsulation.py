class MyClass:
    #Class variables
    var1= "Hello"
    var2= "World"

    #Constructor and Instance variables
    def __init__(self,dynamic_var1,dynamic_var2,dynamic_var3):
        self.dynamic_var1= dynamic_var1 #public variable
        self.__dynamic_var2= dynamic_var2 #private variable
        self._dynamic_var3= dynamic_var3 #protected variable
        print("Inside constructor")

    def display(self):
        print("Inside display method, dynamic_var1 is:", self.dynamic_var1)
    def display1(self):
        print(f"Inside display1 method, dynamic_var2 is: {self.__dynamic_var2}")
    def display2(self):
        print(f"Inside display2 method, dynamic_var3 is: {self._dynamic_var3}")

obj1= MyClass("Dynamic Hello","Dynamic World","Dynamic Value")
print("obj1.dynamic_var1:",obj1.dynamic_var1)
print("obj1.__dynamic_var2:",obj1.__dynamic_var2) #Throw an error because __dynamic_var2 is private and cannot be accessed outside the class
print("obj1._dynamic_var3:",obj1._dynamic_var3) #This is a protected variable and can be accessed within the class and its subclasses
#obj1.__dynamic_var2= "New Value" #Throw an error because __dynamic_var2 is private and cannot be accessed outside the class