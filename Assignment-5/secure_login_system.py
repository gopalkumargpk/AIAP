import bcrypt
import sqlite3
import re
from pathlib import Path
import os
from datetime import datetime, timedelta
from typing import Tuple, Optional
import secrets
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LoginSystem:
    def __init__(self):
        self.db_file = 'users.db'
        self._initialize_database()
        self.max_attempts = 3
        self.lockout_duration = timedelta(minutes=15)
        self.min_password_length = 12
        # Get pepper from environment variable or generate a new one
        self.pepper = os.getenv('PASSWORD_PEPPER', secrets.token_hex(32))
        
    def _initialize_database(self) -> None:
        """Initialize SQLite database with proper schema"""
        with sqlite3.connect(self.db_file) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    failed_attempts INTEGER DEFAULT 0,
                    last_attempt_time TIMESTAMP,
                    locked_until TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP
                )
            ''')
            conn.execute('PRAGMA journal_mode=WAL')  # Enable Write-Ahead Logging for better concurrency
    
    def _hash_password(self, password: str) -> bytes:
        """
        Hash password using bcrypt with pepper
        """
        # Combine password with pepper before hashing
        peppered_password = f"{password}{self.pepper}".encode('utf-8')
        # Generate a random salt and hash the password
        salt = bcrypt.gensalt(rounds=12)  # Work factor of 12 for good security/performance balance
        return bcrypt.hashpw(peppered_password, salt)
    
    def _verify_password(self, password: str, hashed: bytes) -> bool:
        """
        Verify password against stored hash
        """
        peppered_password = f"{password}{self.pepper}".encode('utf-8')
        try:
            return bcrypt.checkpw(peppered_password, hashed)
        except ValueError:
            return False
    
    def _validate_password_strength(self, password: str) -> Tuple[bool, str]:
        """
        Validate password strength with enhanced requirements
        """
        if len(password) < self.min_password_length:
            return False, f"Password must be at least {self.min_password_length} characters long"
        
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter"
        
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter"
        
        if not re.search(r'[0-9]', password):
            return False, "Password must contain at least one number"
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False, "Password must contain at least one special character"
        
        # Check for common patterns
        if any(pattern in password.lower() for pattern in ['password', '123', 'qwerty', 'admin']):
            return False, "Password contains common patterns that are not allowed"
        
        return True, "Password meets security requirements"
    
    def _is_account_locked(self, username: str) -> Tuple[bool, Optional[str]]:
        """Check if account is locked and handle lockout expiry"""
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.execute('''
                SELECT failed_attempts, locked_until
                FROM users
                WHERE username = ?
            ''', (username,))
            result = cursor.fetchone()
            
            if result:
                failed_attempts, locked_until = result
                if locked_until and datetime.fromisoformat(locked_until) > datetime.now():
                    time_remaining = datetime.fromisoformat(locked_until) - datetime.now()
                    return True, f"Account is locked. Try again in {time_remaining.seconds // 60} minutes"
                elif locked_until:
                    # Reset lockout if duration has passed
                    conn.execute('''
                        UPDATE users
                        SET failed_attempts = 0, locked_until = NULL
                        WHERE username = ?
                    ''', (username,))
                    conn.commit()
            
            return False, None

    def register(self, username: str, password: str) -> Tuple[bool, str]:
        """Register a new user with secure password hashing"""
        # Validate username
        if not username or len(username) < 3:
            return False, "Username must be at least 3 characters long"
        
        if not re.match(r'^[a-zA-Z0-9_-]+$', username):
            return False, "Username can only contain letters, numbers, underscores, and hyphens"
        
        # Validate password strength
        is_valid, message = self._validate_password_strength(password)
        if not is_valid:
            return False, message
        
        try:
            with sqlite3.connect(self.db_file) as conn:
                password_hash = self._hash_password(password)
                conn.execute('''
                    INSERT INTO users (username, password_hash)
                    VALUES (?, ?)
                ''', (username, password_hash))
                return True, "Registration successful"
        except sqlite3.IntegrityError:
            return False, "Username already exists"
        except Exception as e:
            return False, "Registration failed due to system error"

    def login(self, username: str, password: str) -> Tuple[bool, str]:
        """Authenticate a user with secure password verification"""
        try:
            # Check for account lockout
            is_locked, lock_message = self._is_account_locked(username)
            if is_locked:
                return False, lock_message
            
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.execute('''
                    SELECT password_hash, failed_attempts
                    FROM users
                    WHERE username = ?
                ''', (username,))
                result = cursor.fetchone()
                
                if not result:
                    # Use consistent timing for non-existent users
                    bcrypt.hashpw(b'dummy_password', bcrypt.gensalt())
                    return False, "Invalid username or password"
                
                stored_hash, failed_attempts = result
                
                if self._verify_password(password, stored_hash):
                    # Successful login - reset failed attempts and update last login
                    conn.execute('''
                        UPDATE users
                        SET failed_attempts = 0,
                            locked_until = NULL,
                            last_login = CURRENT_TIMESTAMP
                        WHERE username = ?
                    ''', (username,))
                    return True, "Login successful"
                else:
                    # Failed login attempt
                    new_failed_attempts = failed_attempts + 1
                    if new_failed_attempts >= self.max_attempts:
                        locked_until = datetime.now() + self.lockout_duration
                        conn.execute('''
                            UPDATE users
                            SET failed_attempts = ?,
                                locked_until = ?
                            WHERE username = ?
                        ''', (new_failed_attempts, locked_until.isoformat(), username))
                        return False, f"Account locked due to too many failed attempts. Try again in {self.lockout_duration.seconds // 60} minutes"
                    else:
                        conn.execute('''
                            UPDATE users
                            SET failed_attempts = ?,
                                last_attempt_time = CURRENT_TIMESTAMP
                            WHERE username = ?
                        ''', (new_failed_attempts, username))
                        return False, "Invalid username or password"
                
        except Exception as e:
            return False, "Login failed due to system error"

def main():
    login_system = LoginSystem()
    
    while True:
        print("\n=== Secure Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                success, message = login_system.register(username, password)
                print(f"\n{message}")
                
            elif choice == '2':
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                success, message = login_system.login(username, password)
                print(f"\n{message}")
                if success:
                    print(f"Welcome, {username}!")
                    
            elif choice == '3':
                print("\nGoodbye!")
                break
                
            else:
                print("\nInvalid choice. Please try again.")
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
        except Exception as e:
            print("\nAn error occurred. Please try again.")

if __name__ == "__main__":
    main()