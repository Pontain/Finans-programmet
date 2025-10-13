import json
import os
from datetime import datetime
from enum import Enum


class TransactionType(Enum): #Fråga användare ""på UI"" om det här är 0 = expense eller...
    UTGIFT = 0
    INKOMST = 1


class GetValues:
    @staticmethod
    def get_transaction_date():
        transaction_date = datetime.today().strftime("%Y-%m-%d-%H")
        return transaction_date

    @staticmethod
    def get_transaction_amount(amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Belopp kan inte vara noll eller negativt!")
                return False
            return amount
        except ValueError:
            print("Ange ett giltigt belopp (större än 0):")
            return False

    @staticmethod
    def get_transaction_type(type_):
        if type_ not in [TransactionType.UTGIFT.value, TransactionType.INKOMST.value]:
            print("Ogiltig typ! Välj 0 = Utgift eller 1 = Inkomst")
            return False
        return type_

    @staticmethod
    def print_transaction_categories(transaction_type):
        if transaction_type == "0":
            categories = ["Mat", "Hyra", "Transport", "Shopping", "Annat"]

        else:
            categories = ["Lön", "Bonus", "Gåva", "Annat"]

        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")
        return categories

    @staticmethod
    def get_transaction_category(self, transaction_type, category):
        categories = self.print_transaction_categories(transaction_type)

        while True:
            if category.isdigit():
                category = int(category)
                if 1 <= category <= len(categories):
                    return categories[category - 1]  # return category name
            print(f"Ogiltigt val! Ange ett nummer mellan 1 och {len(categories)}.")


class DataManager:
    def __init__(self):
        self.transactions: list = []

    @staticmethod
    def generate_file_name():
        today = datetime.today().strftime('%Y-%m')
        return f"transaktion_{today}.json"

    def load_months_transactions(self):
        file_name = self.generate_file_name()
        if not os.path.exists(file_name):
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump([],file, indent=4)
            return []
        else:
            with open(file_name, 'r', encoding="utf-8") as f:
                month_transactions = json.load(f)
                return month_transactions

    def save_months_transactions(self):
        file_name = self.generate_file_name()
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                json.dump([],f, indent=4)
        else:
            with open(file_name, 'w') as f:
                json.dump(self.transactions,f, indent=4)


    # User can print the transaction once created (not mandatory)
    def save_latest_transaction(self, amount, type_, category):
        transaction = self.create_new_transaction(amount, type_, category)
        with open("My_transaktion.json", 'w', encoding="utf-8") as f:
            json.dump(transaction, f, indent=4)

        print("Senaste transaktionen:")
        print(f"  Belopp: {transaction['amount']}")
        print(f"  Kategori: {transaction['category']}")
        print(f"  Typ: {transaction['type_']}")
        print(f"  Datum: {transaction['date']}")

    #..................................................................................................



    @staticmethod
    def create_new_transaction(amount, type_, category):

        amount = GetValues.get_transaction_amount(amount)
        type_ = GetValues.get_transaction_type(type_)
        category = GetValues.get_transaction_category(category)
        date = GetValues.get_transaction_date()

        new_transaction = {"amount": amount,
                           "category": category,
                           "type_": type_,
                           "date": date}

        return new_transaction

        # User can download a file containing one transaction

    def get_months_transactions(self):
        month_transactions = self.load_months_transactions()

        if not month_transactions:
            print("Inga transaktioner den här månaden.")
            return

        print("Månads transaktioner:")
        for i, transaction in enumerate(month_transactions, start=1):
            print(
                f"{i}. Belopp: {transaction['amount']}, Kategori: {transaction['category']}, Typ: {transaction['type_']}, Datum: {transaction['date']}")


