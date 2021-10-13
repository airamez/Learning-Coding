# Class implementation example
# Encapsulation in Python is define by name convention
# Protected attributes starts with _
# Private attributes starts with __
class Account:
    '''Class representing a Bank Account'''
    def __init__(self, id: str, balance: float):
        '''Constrcutor '''
        self.__id = id  # private attribute
        self.__balance = balance  # private attribute

    def setId(self, id):
        '''Set ID (Setter for ID)'''
        self.__id = id

    def getId(self):
        '''Get ID (Getter for ID)'''
        return self.__id

    def getBalance(self):
        '''Get Balance'''
        return self.__balance

    def deposit(self, amount: float):
        '''Deposit the amount to the Account balance '''
        self.__balance += amount

    def withdraw(self, amount: float):
        '''Withdraw the amount from the Account balance'''
        self.__balance -= amount

    def __privateMethod():  # Private method
        pass


account_1 = Account(0, 1000)
account_2 = Account(2, 2000)

print('Account 1: ', account_1.getId(), account_1.getBalance())
print('Account 2: ', account_2.getId(), account_2.getBalance())

account_1.setId(1)
print('Account 1: ', account_1.getId(), account_1.getBalance())

account_1.deposit(500)
print('Account 1: ', account_1.getId(), account_1.getBalance())
account_1.withdraw(1000)
print('Account 1: ', account_1.getId(), account_1.getBalance())

print('Account 1: ', account_1.getId(), account_1.getBalance())
try:
    print('account_1.__balance =', account_1.__balance)
except Exception as ex:
    print('account_1.__balance is private: ', ex)

try:
    account_1.__privateMethod()
except Exception as ex:
    print('account_1.__privateMethod is private: ', ex)

# As Python allow attributes to be created on the fly.
# The operation below will create a different attribute
# ATTENTION: Use the debugger to demonstrate
account_1.__balance = 10000  # This will be a different attribute
print('account_1.__balance =', account_1.__balance)
print('Account 1: ', account_1.getId(), account_1.getBalance())
