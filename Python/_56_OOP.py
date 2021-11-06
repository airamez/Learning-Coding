# As python allow the "creation" of classe attributes on the fly
# It is possible to use a empty class as an abstract type


class Customer:
    pass


customers = list()

customer1 = Customer()
customer1.FistName = 'Bob'
customer1.LastName = 'Marley'
customer1.Email = 'bob.marley@heaven.com'

customer2 = Customer()
customer2.FistName = 'Michael'
customer2.LastName = 'Jackson'
customer2.Email = 'michael.jackson@email.com'

customer3 = Customer()
customer3.FistName = 'Frank'
customer3.LastName = 'Sinata'
customer3.Email = 'frank.sinatra@email.com'

customers.append(customer1)
customers.append(customer2)
customers.append(customer3)

for c in customers:
    print(f"Name: {c.FistName} {c.LastName}; Email: {c.Email}")
