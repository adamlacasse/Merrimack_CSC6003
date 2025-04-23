from models.user import User

# Object to store users in memory
users = {}

def add_user(name):
    if name in users:
        return f"User '{name}' already exists."
    users[name] = User(name)
    return f"User '{name}' added successfully."

def change_user(name):
    if name not in users:
        return f"User '{name}' not found."
    return f"User changed to '{name}'." 

def get_user(name):
    return users.get(name)
