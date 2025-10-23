from models.user import User
import pandas as pd

class FinanceTracker:
    def __init__(self, user: User):
        self.user = user
        self.user_id = user.user_id
        self.categories = []
        self.transaction = []
        self.paychecks = []
    
    def __str__(self) -> str:
        return f"FinanceTracker for {self.user.username}"