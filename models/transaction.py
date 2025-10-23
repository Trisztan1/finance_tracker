from models.id_generation import ID
from models.category import Category
from models.user import User
import datetime

class Transaction:
    def __init__(self, user: User, amount: float, category: Category, description: str="", date: datetime.date | None = None, unique_id = None):
        self.user_id = user.user_id
        self.date = date or datetime.date.today()
        self.amount = amount
        self.category_id = category.category_id
        self.type = category.type
        self.description = description
        self.unique_id = unique_id or ID.generate_timestamp_id()
    
    #### Set amount ####
    @property
    def amount(self) -> float:
        return self._amount
    
    @amount.setter
    def amount(self, amount: float | int):
        if not isinstance(amount, (float, int)):
            raise ValueError("Input is not a number")
        self._amount = float(amount)
    
    #### Set date ####
    @property 
    def date(self) -> datetime.date:
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, datetime.date):
            raise ValueError("Date must be a datetime.date object")
        self._date = date

    
    def to_row(self) -> dict:
        return {
            "user_id": self.user_id,
            "date": self.date,
            "amount": self.amount,
            "category_id": self.category_id,
            "type": self.type,
            "description": self.description,
            "transaction_id": self.unique_id
        }
    
    # This is wrong, you have to update it, but first write FinanceTracker class
    @classmethod
    def from_row(cls, row):
        user = User(row["user"], password="")
        category = Category(row["category"], row["type"])
        date = datetime.datetime.strptime(row["date"], "%Y-%m-%d").date()

        return cls(
            user = user,
            amount = float(row["amount"]),
            category = category,
            description = row.get("description", ""),
            date = date
        )
            

    
class Paychecks(Transaction):
    def __init__(self, user, amount: float, budget: float, date = None, description = None):
        paycheck_category = Category("paycheck", "income")

        super().__init__(user, amount, category = paycheck_category, date = date, description = description)
        self.budget = budget
    
    @property
    def budget(self) -> float:
        return self._budget
    
    @budget.setter
    def budget(self, budget: float | int):
        if not isinstance(budget, (float, int)):
            raise ValueError("Input is not a number")
        self._budget = float(budget)

    def to_row(self) -> dict:
        parent_row = super().to_row()
        return {
            "user_id": parent_row["user_id"],
            "date": parent_row["date"],
            "amount": parent_row["amount"],
            "category_id": parent_row["category_id"],
            "type": parent_row["type"],
            "budget": self.budget,
            "description": parent_row["description"],
            "paycheck_id": parent_row["transaction_id"]
        }