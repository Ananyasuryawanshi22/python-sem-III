class Printer:
    printer = None

    def __new__(cls):
        if cls.printer is None:
            cls.printer = super().__new__(cls)
        return cls.printer

    def print_document(self, document):
        print("Printing:", document)


user1 = Printer()
user1.print_document("Assignment.pdf")

user2 = Printer()
user2.print_document("Report.docx")

if user1 is user2:
    print("Both users are using the same printer object.")
else:
    print("Different printer objects exist.")