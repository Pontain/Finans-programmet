🗂 Project Structure
personal_budget_manager/
│
├── data_manager.py ---Kosar
├── budget_manager.py---Ali
├── report_manager.py---- Hampus
├── ui_manager.py-----Pontus
└── main.py

🧱 data_manager.py
class DataManager:
    def __init__(self):
        pass

    def load_data(self):
        pass

    def save_data(self, data):
        pass

    def add_transaction(self, amount, category, type_):
        pass

    def get_all_transactions(self):
        pass


budget_manager.py
class BudgetManager:
    def __init__(self, data_manager):
        pass

    def set_budget(self, category, amount):
        pass

    def get_budget(self, category):
        pass

    def check_budget(self):
        pass

📊 report_manager.py
class ReportManager:
    def __init__(self, data_manager):
        pass

    def summary_report(self):
        pass

    def show_expense_by_category(self):
        pass

    def show_income_vs_expense(self):
        pass

🧑‍💻 ui_manager.py
class UIManager:
    def __init__(self, data_manager, budget_manager, report_manager):
        pass

    def main_menu(self):
        pass

    def add_income(self):
        pass

    def add_expense(self):
        pass

    def set_budget(self):
        pass

    def show_reports(self):
        pass

    def check_budgets(self):
        pass

▶️ main.py
from data_manager import DataManager
from budget_manager import BudgetManager
from report_manager import ReportManager
from ui_manager import UIManager

def main():
    data_manager = DataManager()
    budget_manager = BudgetManager(data_manager)
    report_manager = ReportManager(data_manager)
    ui = UIManager(data_manager, budget_manager, report_manager)
    ui.main_menu()

if __name__ == "__main__":
    main()
