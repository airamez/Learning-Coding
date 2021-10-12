# OO in pratice

class Account:
  '''Class representing a Bank Account'''

  def __init__(self, id: str, balance: float):
    '''Constrcutor '''
    self.__id = id # private attribute
    self.__balance = balance # private attribute

  # Defining a property for ID
  @property
  def ID(self):
    '''Get ID'''
    return self.__id

  @ID.setter
  def ID(self, value):
    # The power of encapsulation
    if not value or not value.strip():
      raise ValueError("Account Id is required")
    self.__id = value

  @property # balance has no setter (The power of encapualation)
  def balance(self):
    '''Get Balance'''
    return self.__balance
  
  def deposit(self, amount: float):
    '''Deposit the amount to the Account balance '''
    self.__balance += amount;

  def withdraw(self, amount: float):
    '''Withdraw the amount from the Account balance'''
    self.__balance -= amount;


class Customer:
  '''Class representing a Customer'''

  def __init__(self, name: str, email: str):
    self.__name = name
    self.__email = email
    self.__accounts = dict()

  @property
  def Name(self):
    return self.__name

  @Name.setter
  def Name(self, value):
    if not value or not value.strip():
        raise ValueError("name Id is required")
    self.__name = value
  
  @property
  def Email(self):
    return self.__email

  @Email.setter
  def Email(self, value):
    if not value or not value.strip():
        raise ValueError("name Id is required")
    self.__name = value

  def AddAccount(self, id: str, balance: float):
    newAccount = Account(id, balance)
    self.Accounts[newAccount.id] = newAccount

  @property
  def Account(self, id: str):
    if id in self.__accounts.keys:
      return self.__accounts[id]
    else:
      raise ValueError(f"Account not found for this client: ID = {id}")
