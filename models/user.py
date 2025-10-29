from models.category import Category
from models.id_generation import ID


class User:
    def __init__(self, username: str, password: str, categories: list | None = None, user_id: str | None = None):
        self.username = username
        self.password = password
        self.categories = categories
        self.user_id = user_id or ID.generate_timestamp_id()

    def __repr__(self) -> str:
        return f"User(username='{self.username}', user_id='{self.user_id}')"

    def __str__(self) -> str:
        return f"User: {self.username} (ID: {self.user_id})"
    
    @property
    def categories(self):
        return self._categories
    
    @categories.setter
    def categories(self, categories) -> list:
        if categories is None:
            self._categories = [
                Category("food", "expense"),
                Category("snacks", "expense"),
                Category("rent", "expense"),
                Category("utilities", "expense"),
                Category("transportation", "expense"),
                Category("clothing", "expense"),
                Category("health", "expense"),
                Category("entertainment", "expense"),
                Category("tech", "expense"),
                Category("education", "expense"),
                Category("other expenses", "expense")
            ]
        else:
            self._categories = categories

    def to_row(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "user_id": self.user_id
        }
    