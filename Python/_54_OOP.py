from _53_OOP_05 import Customer

customer1 = Customer('Jose Santos', 'airamez@gmail.com')
customer1.AddAccount('1', 1000)
customer1.GetAccount('1').deposit(500)
customer1.GetAccount('1').deposit(250)
customer1.GetAccount('1').withdraw(750)

print("Customer", customer1.Name, customer1.Email)
print("Balance", customer1.GetAccount('1').Balance)
print(customer1.GetAccount('1').Statement)

customer1.GetAccount('1').withdraw(5000)