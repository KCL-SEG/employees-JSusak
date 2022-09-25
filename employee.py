"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    # Boolean for if the employee is on salary or hourly. Default is salary.
    def __init__(self, name, commissiontype=None):

        self.name = name
        self.commission = commissiontype
        self.salamount = 0
        self.employeetype = None
        self.hourwage = 0
        self.hours = 0

        self.bonusamount = 0

        self.contracts = 0
        self.contractprices = 0

    def add_contracts(self, contractamount, contractprice):
        self.contracts = contractamount
        self.contractprices = contractprice

    def add_bonus(self, bonusamount):
        self.bonusamount = bonusamount

    def add_commission(self):
        if self.commission is None:
            return 0
        elif self.commission == "bonus" and self.bonusamount > 0:
            return self.bonusamount
        # Contract
        elif self.commission == "contract" and self.contracts > 0 and self.contractprices > 0:
            return self.contracts * self.contractprices
        else:
            raise ValueError("Invalid commission types...")

    def get_pay(self):
        if self.salamount > 0:
            return self.salamount + self.add_commission()
        else:
            return (self.hourwage * self.hours) + self.add_commission()

    def __str__(self):
        str = f"{self.name} works on "
        if self.employeetype == "salary":
            str += f"a monthly salary of {self.salamount}"
        else:
            str += f"a contract of {self.hours} hours at {self.hourwage}/hour"



        if self.commission is None:
            str += "."
        elif self.commission == "bonus":
            str += f" and receives a bonus commission of {self.add_commission()}."
        # Contract
        else:
            str += f" and receives a commission for {self.contracts} contract(s) at {self.contractprices}/contract."

        str += f"  Their total pay is {self.get_pay()}."

        return str


class SalaryEmployee(Employee):
    def __init__(self, name, salamount, commissiontype=None):
        super().__init__(name, commissiontype)
        self.employeetype = "salary"
        self.salamount = salamount


class HourlyEmployee(Employee):
    def __init__(self, name, hourwage, hours, commissiontype=None):
        super().__init__(name, commissiontype)
        self.employeetype = "hourly"
        self.hourwage = hourwage
        self.hours = hours


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)
billie.__str__()
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)
charlie.__str__()

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee',3000, "contract")
renee.add_contracts(4,200)
renee.__str__()

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan',25,150,"contract")
jan.add_contracts(3,220)
jan.__str__()

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie',2000,"bonus")
robbie.add_bonus(1500)
robbie.__str__()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel',30,120,"bonus")
ariel.add_bonus(600)
ariel.__str__()
