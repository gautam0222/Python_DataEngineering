class company:

    title:str = "cosultancy"
    def __init__(self, company_name:str):
        self.company_name= company_name

    def info(self):
        print(f"Company Name: {self.company_name}")
        return self.company_name

class employee(company):
    def __init__(self, company_name:str, employee_name:str):
        self.company_name= company_name
        self.employee_name= employee_name

    def info(self): #if a method is defined in the child class with the same name as the parent class, it will override the parent class method
        response= company.info(self)
        print(f"Company Name: {response}, Employee Name: {self.employee_name}")

class contractor(company):
    def __init__(self, company_name:str, contractor_name:str):
        self.company_name= company_name
        self.contractor_name= contractor_name

    def info(self):
        response= company.info(self)
        print(f"Company Name: {response}, Contractor Name: {self.contractor_name}")

obj= employee("TCS", "John Doe")
obj.info()

obj2= contractor("Infosys", "Jane Smith")
obj2.info()