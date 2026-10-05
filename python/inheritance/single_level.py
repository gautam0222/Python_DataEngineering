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

    def employee_info(self):
        response= company.info(self)
        print(f"Company Name: {response}, Employee Name: {self.employee_name}")

if __name__ == "__main__":
    obj = employee("TCS", "John Doe")
    obj.employee_info()
