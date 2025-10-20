# -*- coding: utf-8 -*-
# Author: Ali
# budget_manager.py 

class BudgetManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def set_budget(self, category, amount):
        self.data_manager.set_budget(category, amount)

    def get_budget(self, category):
        return self.data_manager.get_budget(category)

    def check_budget(self):
        
        budgets = self.data_manager.get_all_budgets()
        transactions = self.data_manager.get_all_transactions()

        # compute spent by category manually
        spent = {}
        for t in transactions:
            if t["type"] == "expense":
                category = t["category"]
                amount = float(t["amount"])
                if category not in spent:
                    spent[category] = amount
                else:
                    spent[category] += amount

        results = []
        for category in budgets:
            budget_amount = float(budgets[category])
            used = spent.get(category, 0.0)
            if budget_amount > 0:
                percent = (used / budget_amount) * 100
            else:
                percent = 0.0
            results.append((category, budget_amount, used, percent))

        return results
