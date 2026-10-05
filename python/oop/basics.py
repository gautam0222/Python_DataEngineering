class MyClass:
    #Class variables
    var1= "Hello"
    var2= "World"

    def display(self):
        print("Inside display method")
        print(self.var1)
    def display1(self):
        print("Inside display1 method")
        print(self.var2)

def main() -> None:
    obj1 = MyClass()
    obj1.display()
    obj2 = MyClass()
    obj2.display1()


if __name__ == "__main__":
    main()
