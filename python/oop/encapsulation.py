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

def main() -> None:
    obj1 = MyClass("Dynamic Hello", "Dynamic World", "Dynamic Value")
    print("Public:", obj1.dynamic_var1)
    print("Protected by convention:", obj1._dynamic_var3)
    print("Name-mangled attribute:", obj1._MyClass__dynamic_var2)


if __name__ == "__main__":
    main()
