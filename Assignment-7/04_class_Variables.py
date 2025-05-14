class Bank:
    bank_name = "HBL"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
print(Bank.bank_name)
Bank.change_bank_name("UBL")
print(b1.bank_name)