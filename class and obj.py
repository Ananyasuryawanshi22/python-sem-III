# Decorator
def format_report(func):
    def display(self):
        print(" Report ")
        func(self)
    return display


class Report:
    company = "MIT ADT"

    def __init__(self, title):
        self.title = title

    def set_company(cls, name):
        cls.company = name

    def set_comapny(self,name):
        Report.company=name 
        
    def show(self):
        print("Company:", Report.company)
        print("Title:", self.title)


# Main Program
r = Report("Annual Report")
Report.set_company("ABC Pvt Ltd")
r.show()