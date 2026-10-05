class MyClass:
    #Class variables
    var1= "Hello"
    var2= "World"

    #Constructor and Instance variables
    def __init__(self,dynamic_var1,dynamic_var2):
        self.dynamic_var1= dynamic_var1
        self.dynamic_var2= dynamic_var2
        print("Inside constructor")

    def display(self):
        print("Inside display method, dynamic_var1 is:", self.dynamic_var1)
        print(self.var1)
    def display1(self):
        print(f"Inside display1 method, dynamic_var2 is: {self.dynamic_var2}")
        print(self.var2)

def main() -> None:
    obj1 = MyClass("Dynamic Hello", "Dynamic World")
    obj1.display()
    obj2 = MyClass("Dynamic Hello", "Dynamic World")
    obj2.display1()

    obj1.var1 = "Hello1"
    print("obj1.var1:", obj1.var1)


if __name__ == "__main__":
    main()
