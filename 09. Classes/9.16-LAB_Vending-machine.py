"""
9.16 LAB: Vending machine
Natalie Nguyen - IS 640

Given two integers as user inputs that represent the number of drinks to buy and the number of bottles to restock, 
create a VendingMachine object that performs the following operations:

    - Purchases input number of drinks
    - Restocks input number of bottles
    - Reports inventory

A VendingMachine's initial inventory is 20 drinks.
"""

class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    customer = VendingMachine()
    
    # TODO: Purchase input number of drinks
    customer.purchase(int(input()))
    
    # TODO: Restock input number of bottles
    customer.restock(int(input()))
    
    # TODO: Report inventory
    customer.report()