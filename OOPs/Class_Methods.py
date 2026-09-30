class MyClass:

    my_var=100

    def change_var(self, new_value:int):
        MyClass.my_var= new_value

    @classmethod #class method takes cls as the first parameter
    def _class_method(cls, new_value:int):
        cls.my_var= new_value

    @staticmethod #static method does not take self or cls as the first parameter
    def _static_method(new_value:int):
        MyClass.my_var= new_value

obj1= MyClass()
obj1.change_var(200)
print(obj1.my_var)  # Output: 200
obj2= MyClass()
print(obj2.my_var)  # Output: 200
obj1._static_method(300)
print(obj1.my_var)  # Output: 300
print(obj2.my_var)  # Output: 300