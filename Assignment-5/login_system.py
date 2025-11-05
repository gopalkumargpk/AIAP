import hashlib
import json
from pathlib import Path
import re

class LoginSystem:
    def __init__(self):
        self.users_file = 'users.json'
        self._initialize_users_file()
    
    def _initialize_users_file(self):
        """Initialize the users file if it doesn't exist"""
        if not Path(self.users_file).exists():
            with open(self.users_file, 'w') as f:
                json.dump({}, f)
    
    def _hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _validate_password_strength(self, password):
        """
        Validate password strength
        Requirements:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one number
        - Contains at least one special character
        """
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter"
        
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter"
        
        if not re.search(r'[0-9]', password):
            return False, "Password must contain at least one number"
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False, "Password must contain at least one special character"
        
        return True, "Password meets all requirements"

    def register(self, username, password):
        """Register a new user"""
        # Load existing users
        with open(self.users_file, 'r') as f:
            users = json.load(f)
        
        # Check if username already exists
        if username in users:
            return False, "Username already exists"
        
        # Validate password strength
        is_valid, message = self._validate_password_strength(password)
        if not is_valid:
            return False, message
        
        # Hash password and store user
        hashed_password = self._hash_password(password)
        users[username] = {
            'password': hashed_password,
            'failed_attempts': 0,
            'locked': False
        }
        
        # Save updated users
        with open(self.users_file, 'w') as f:
            json.dump(users, f)
        
        return True, "Registration successful"

    def login(self, username, password):
        """Login a user"""
        # Load users
        with open(self.users_file, 'r') as f:
            users = json.load(f)
        
        # Check if user exists
        if username not in users:
            return False, "Invalid username or password"
        
        user = users[username]
        
        # Check if account is locked
        if user.get('locked', False):
            return False, "Account is locked due to too many failed attempts"
        
        # Verify password
        if self._hash_password(password) != user['password']:
            # Increment failed attempts
            user['failed_attempts'] = user.get('failed_attempts', 0) + 1
            
            # Lock account after 3 failed attempts
            if user['failed_attempts'] >= 3:
                user['locked'] = True
                message = "Account has been locked due to too many failed attempts"
            else:
                message = "Invalid username or password"
            
            # Save updated user data
            with open(self.users_file, 'w') as f:
                json.dump(users, f)
                
            return False, message
        
        # Reset failed attempts on successful login
        user['failed_attempts'] = 0
        with open(self.users_file, 'w') as f:
            json.dump(users, f)
        
        return True, "Login successful"

# Example usage
def main():
    login_system = LoginSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = login_system.register(username, password)
            print(message)
            
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = login_system.login(username, password)
            print(message)
            if success:
                print(f"Welcome, {username}!")
                
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()