# using properties to replace the setter and getters Methods
class Account:
    '''Class representing a Bank Account'''
    def __init__(self, id: str, balance: float):
        '''Constrcutor '''
        self.__id = id  # private attribute
        self.__balance = balance  # private attribute

    # Defining a property for ID
    @property
    def id(self):
        '''Get ID'''
        return self.__id

    @id.setter
    def id(self, value):
        # The power of encapsulation
        if not value or not value.strip():
            raise ValueError("Account Id is required")
        self.__id = value

    @property  # balance has no setter (The power of encapualation)
    def balance(self):
        '''Get Balance'''
        return self.__balance

    def deposit(self, amount: float):
        '''Deposit the amount to the Account balance '''
        self.__balance += amount

    def withdraw(self, amount: float):
        '''Withdraw the amount from the Account balance'''
        self.__balance -= amount


account_1 = Account(0, 1000)
account_2 = Account(2, 2000)

try:
    account_1.id = ''
except ValueError as ex:
    print(ex)

account_1.id = "1"

print('Account 1: ', account_1.id, account_1.balance)
print('Account 2: ', account_2.id, account_2.balance)

account_1.deposit(500)
print('Account 1: ', account_1.id, account_1.balance)
account_1.withdraw(1000)
print('Account 1: ', account_1.id, account_1.balance)
