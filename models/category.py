from models.id_generation import ID

class Category:
    def __init__(self, name: str, type: str, budget: float = 0, category_id = None):
        self.name = name
        self.type = type
        self.budget = budget
        self.category_id = category_id or ID.generate_timestamp_id()


    #### Set Type ####
    @property
    def type(self) -> str:
        return self._type
    
    @type.setter
    def type(self, type):
        if type not in ["income", "expense"]:
            raise ValueError("Invalid type")
        self._type = type

    #### Set budget ####
    @property
    def budget(self) -> float:
        return self._budget
    
    @budget.setter
    def budget(self, amount: float | int):
        if not isinstance(amount, (float, int)):
            raise ValueError("Input is not a number")
        self._budget = float(amount)

    def to_row(self):
        return {
            "name": self.name,
            "type": self.type,
            "budget": self.budget,
            "category_id": self.category_id
        }