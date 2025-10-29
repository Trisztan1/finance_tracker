from models.category import Category
from models.finance_tracker import FinanceTracker
from models.transaction import Transaction, Paychecks
from models.user import User
from models.id_generation import ID
from models.user_manager import UserManager
import time

user_manager = UserManager()


user = user_manager.authenticate_user("matilda", "mati123")

user_tracker = user_manager.login_user(user)

user_manager.delete_account(user)

user_manager.save_users()


print(user_manager.username_dict)
print()
print(user_manager.users)
print()
# print(f"{user.username}///{user.user_id}")
# print(user_tracker)
# print(user_manager.username_dict)

# wage = Paychecks(u, 50000, 10000)

# id = ID.generate_timestamp_id()

# flag = True

# while flag == True:
    
#     check = input("Do you want to check wage: ").strip().lower()
#     if check == "yes":
#         print(Paychecks.to_row(wage))
#         print(f"\n{id}\n")
#     elif check == "exit":
#         flag = False
#     else:
#         continue
