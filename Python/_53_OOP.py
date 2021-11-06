# OO in pratice
from datetime import datetime


class Account:
    def __init__(self, id: str, balance: float):
        self.__id = id  # ID
        self.__balance = balance  # Balance
        self.__transactions = list()

    @property
    def ID(self):
        return self.__id

    @ID.setter
    def ID(self, value):
        if not value or not value.strip():
            raise ValueError("Account Id is required")
        self.__id = value

    @property
    def Balance(self):
        return self.__balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__transactions.append(
            self.__getTransactionFormated("Deposit", amount))

    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError(
                f'Not enough balance: Balance = {self.__balance}; Amount = {amount}'
            )
        self.__balance -= amount
        self.__transactions.append(
            self.__getTransactionFormated("Withdraw", amount))

    @property
    def Statement(self):
        statement = '{ statement: ['
        for transaction in self.__transactions:
            statement += transaction
        statement += "\n]}"
        return statement

    def __getCurrentDateTime(self):
        now = datetime.now()
        return now.strftime("%d/%m/%Y %H:%M:%S.%f")

    def __getTransactionFormated(self, type: str, amount: float):
        transaction = f'\n\t{{"datetime": "{self.__getCurrentDateTime()}", "\ttype": {type}, "amount": {amount}}}'
        return transaction


class Customer:
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
        self.__accounts[newAccount.ID] = newAccount

    def GetAccount(self, id: str):
        if id in self.__accounts.keys():
            return self.__accounts[id]
        else:
            raise ValueError(f"Account not found for this client: ID = {id}")
