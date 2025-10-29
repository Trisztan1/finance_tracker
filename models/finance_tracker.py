from datetime import datetime
from models.user import User
from models.transaction import Transaction, Paychecks
from models.user_manager import UserManager
from models.category import Category
import pandas as pd
import csv

class FinanceTracker:
    def __init__(self, user: User):
        self.user = user
        self.user_id = user.user_id
        self.categories = user.categories
        self.categories_by_id = {c.category_id: c for c in self.categories}
        self.transactions = []
        self.transactions_by_id = {}
        self.paychecks = []
        self.load_transactions()
    
    def __str__(self) -> str:
        return f"FinanceTracker for {self.user.username}"
    

    #### TRANSACTION CLASS TRACKER METHODS ####

    #### Transaction Data_Managment Methods ####

    def load_transactions(self):
        try:
            with open(f"data/transactions/{self.user_id}.csv", "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Only load transactions for this user
                    if row["user_id"] != self.user_id:
                        continue

                    category_id = row["category_id"]
                    if category_id not in self.categories_by_id:
                        print(f"Warning: Category ID {category_id} not found for user {self.user.username}")
                        continue
                    category = self.categories_by_id[category_id]

                    tx = Transaction(
                        user = self.user, 
                        amount = float(row["amount"]),
                        category = category,
                        description = row.get("description", ""),
                        date = datetime.strptime(row["date"], "%Y-%m-%d").date(),
                        unique_id = row["transaction_id"]
                        )
                    
                    self.transactions.append(tx)
                    self.transactions_by_id[tx.unique_id] = tx
        except FileNotFoundError:
            print("No transaction.csv found")
        
        except Exception as e:
            print(f"Error loading transactions: {e}")
        
    def save_transactions(self):
        data = []
        for tx in self.transactions:
            data.append(tx.to_row())
        
        with open(f"data/transactions/{self.user_id}.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["user_id", "date", "amount", "category_id", "type", "description", "transaction_id"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(data)
    
    #### Transaction_Management Methods ####

    def add_transaction(self, amount: float, category: Category, description: str | None = None) -> Transaction:
        if category not in self.categories:
            raise ValueError("Can't identify category!")
            
        tx = Transaction(
            user = self.user, 
            amount = float(amount),
            category = category,
            description = description,
        )

        self.transactions.append(tx)
        self.transactions_by_id[tx.unique_id] = tx

        return tx