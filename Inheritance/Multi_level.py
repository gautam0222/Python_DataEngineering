class company:

    title:str = "cosultancy"
    def __init__(self, company_name:str):
        self.company_name= company_name

    def info(self):
        print(f"Company Name: {self.company_name}")
        return self.company_name

class manager(company):
    def __init__(self, company_name:str, manager_name:str):
        self.company_name= company_name
        self.manager_name= manager_name

    def info(self): #if a method is defined in the child class with the same name as the parent class, it will override the parent class method
        response= company.info(self)
        print(f"Company Name: {response}, Manager Name: {self.manager_name}")

class employee(manager):
    def __init__(self, company_name:str, manager_name:str, employee_name:str):
        self.company_name= company_name
        self.manager_name= manager_name
        self.employee_name= employee_name

    def info(self):
        response= manager.info(self)
        print(f"Company Name: {response}, Manager Name: {self.manager_name}, Employee Name: {self.employee_name}")

class contractor(manager):
    def __init__(self, company_name:str, manager_name:str, contractor_name:str):
        self.company_name= company_name
        self.manager_name= manager_name
        self.contractor_name= contractor_name

    def info(self):
        response= manager.info(self)
        print(f"Company Name: {response}, Manager Name: {self.manager_name}, Contractor Name: {self.contractor_name}")

obj= employee("TCS", "Alice Johnson", "John Doe")
obj.info()

obj2= contractor("Infosys", "Alice Johnson", "Jane Smith")
obj2.info()

obj3= manager("Wipro", "Bob Brown")
obj3.info()