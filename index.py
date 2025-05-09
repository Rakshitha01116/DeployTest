# Initial list of users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def create_user(user_list, user_data):
    """Add a new user to the list."""
    if any(user['id'] == user_data['id'] for user in user_list):
        raise ValueError("User with this ID already exists.")
    user_list.append(user_data)

def read_user(user_list, user_id):
    """Retrieve user data by ID."""
    for user in user_list:
        if user['id'] == user_id:
            return user
    return None

def update_user(user_list, user_id, updated_data):
    """Update user data by ID."""
    for user in user_list:
        if user['id'] == user_id:
            user.update(updated_data)
            return True
    return False

def delete_user(user_list, user_id):
    """Delete a user by ID."""
    for i, user in enumerate(user_list):
        if user['id'] == user_id:
            del user_list[i]
            return True
    return False

# Example usage
if __name__ == "__main__":
    print("Initial users:", users)

    # Create
    create_user(users, {"id": 3, "name": "Charlie", "email": "charlie@example.com"})
    print("After adding Charlie:", users)

    # Read
    user = read_user(users, 2)
    print("Read user with ID 2:", user)

    # Update
    update_user(users, 1, {"email": "alice_new@example.com"})
    print("After updating Alice's email:", users)

    # Delete
    delete_user(users, 2)
    print("After deleting user with ID 2:", users)
