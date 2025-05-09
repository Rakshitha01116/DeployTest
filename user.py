import hashlib
users_db = {}

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    """Registers a new user with a hashed password."""
    if username in users_db:
        print("User already exists.")
        return
    hashed = hash_password(password)
    users_db[username] = hashed
    print("Created new user")

def login(username, password):
    """Checks user credentials for login."""
    if username not in users_db:
        print("Username not found.")
        return
    hashed = hash_password(password)
    if users_db[username] == hashed:
        print("Login Successful")
    else:
        print("Invalid password.")

# Example usage
if __name__ == "__main__":
    register("john", "mypassword")   
    login("john", "mypassword")      
    login("john", "wrongpass")
    register("john", "newpass")      
