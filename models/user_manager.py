import csv
from models.finance_tracker import FinanceTracker
from models.user import User

class UserManager:
    def __init__(self):
        self.users = [] # User objects in list
        self.users_dict = {} # key: user_id - value: User object
        self.username_dict = {} # key: username - value: User object
        self.user_trackers = {} # key: user_id - value: FinanceTracker object
        self.load_users()
        
    
    #### USER DATA_MANAGMENT METHODS ####

    # Loading users
    def load_users(self):
        try:
            with open("data/users.csv", "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    user = User(
                        username = row["username"], 
                        password = row["password"], 
                        user_id = row["user_id"]
                        )

                    self.users.append(user)
                    self.user_trackers[user.user_id] = FinanceTracker(user)
                    self.username_dict[user.username] = user
                    self.users_dict[user.user_id] = user
                
                # self.users_dict = {user.user_id: user for user in self.users}
                # this is dict comprehesnion you can do this in this way too

        except FileNotFoundError:
            print("No users.csv found")
        except Exception as e:
            print(f"Error loading users: {e}")
    
    # Saving users
    def save_users(self):
        data = []
        for user in self.users:
            data.append(user.to_row())

        with open("data/users.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["username", "password", "user_id"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(data)


    #### USER MANAGMENT METHODS ####

    # Adding users
    def add_new_user(self, username : str, password : str) -> User:
        for existing_user in self.users:
            if existing_user.username == username:
                raise ValueError(f"User '{username}' already exists")

        user = User(username = username, password = password)
        self.users.append(user)
        self.users_dict[user.user_id] = user
        self.username_dict[user.username] = user
        self.user_trackers[user.user_id] = FinanceTracker(user)
        return user
    

    #### AUTHENTICATION METHODS ####

    def authenticate_user(self, username: str, password: str) -> User:
        """Authenticate user with username and password"""
        if username not in self.username_dict:
            raise ValueError(f"Invalid username: '{username}'")

        user = self.get_user_by_username(username = username)

        if user.password != password:
            raise ValueError(f"Incorrect password!")
        return user


    def login_user(self, user: User) -> FinanceTracker:
        return FinanceTracker(user)


    #### USER LOOKUP METHODS ####

    def get_user_by_username(self, username):
        user = self.username_dict[username]
        return user