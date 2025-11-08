"""Task5: BankAccount Class Implementation

This module implements a BankAccount class that simulates basic banking operations
with proper validation, error handling, and transaction tracking.

Key features:
- Deposit and withdraw operations with amount validation
- Balance checking and transaction history
- Proper error handling for invalid operations
- Transaction timestamps and statement generation
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Literal, Optional


TransactionType = Literal["deposit", "withdrawal"]


@dataclass
class Transaction:
    """Represents a single bank transaction.
    
    Attributes:
        type: Type of transaction (deposit/withdrawal)
        amount: Amount of money involved
        timestamp: When the transaction occurred
        balance_after: Account balance after this transaction
    """
    type: TransactionType
    amount: float
    timestamp: datetime
    balance_after: float


class InsufficientFundsError(Exception):
    """Raised when a withdrawal would result in negative balance."""
    pass


class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid (negative or zero)."""
    pass


class BankAccount:
    """A class representing a bank account with basic operations.
    
    This class maintains account balance and transaction history,
    ensuring all operations maintain valid state and proper records.
    
    Attributes:
        _balance (float): Current account balance (private)
        _transactions (List[Transaction]): History of all transactions
        account_number (str): Unique account identifier
        
    Analysis:
    - All methods operate in O(1) time except get_statement()
    - get_statement() is O(n) where n is number of transactions
    - Memory usage grows linearly with number of transactions
    - Thread-safety not implemented (could add locks if needed)
    """
    
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        """Initialize a new bank account.
        
        Args:
            account_number: Unique identifier for the account
            initial_balance: Starting balance (must be non-negative)
            
        Raises:
            InvalidAmountError: If initial_balance is negative
        """
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative")
            
        self.account_number = account_number
        self._balance = initial_balance
        self._transactions: List[Transaction] = []
        
        # Record initial deposit if any
        if initial_balance > 0:
            self._record_transaction("deposit", initial_balance)
    
    def _validate_amount(self, amount: float) -> None:
        """Validate a transaction amount is positive.
        
        Args:
            amount: Amount to validate
            
        Raises:
            InvalidAmountError: If amount <= 0
        """
        if not isinstance(amount, (int, float)):
            raise InvalidAmountError("Amount must be a number")
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
    
    def _record_transaction(self, type_: TransactionType, amount: float) -> None:
        """Record a transaction in the history.
        
        Args:
            type_: Type of transaction
            amount: Amount involved
        """
        transaction = Transaction(
            type=type_,
            amount=amount,
            timestamp=datetime.now(),
            balance_after=self._balance
        )
        self._transactions.append(transaction)
    
    def deposit(self, amount: float) -> float:
        """Deposit money into the account.
        
        Args:
            amount: Amount to deposit (must be positive)
            
        Returns:
            New balance after deposit
            
        Raises:
            InvalidAmountError: If amount is invalid
        """
        self._validate_amount(amount)
        self._balance += amount
        self._record_transaction("deposit", amount)
        return self._balance
    
    def withdraw(self, amount: float) -> float:
        """Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw (must be positive)
            
        Returns:
            New balance after withdrawal
            
        Raises:
            InvalidAmountError: If amount is invalid
            InsufficientFundsError: If withdrawal would overdraw account
        """
        self._validate_amount(amount)
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance={self._balance}, "
                f"attempted withdrawal={amount}"
            )
        
        self._balance -= amount
        self._record_transaction("withdrawal", amount)
        return self._balance
    
    @property
    def balance(self) -> float:
        """Get current account balance.
        
        Returns:
            Current balance
        """
        return self._balance
    
    def get_statement(self, 
                     start_date: Optional[datetime] = None, 
                     end_date: Optional[datetime] = None) -> List[Transaction]:
        """Get account statement for a date range.
        
        Args:
            start_date: Optional start date (inclusive)
            end_date: Optional end date (inclusive)
            
        Returns:
            List of transactions in the date range
        """
        transactions = self._transactions
        
        if start_date:
            transactions = [t for t in transactions 
                          if t.timestamp >= start_date]
        if end_date:
            transactions = [t for t in transactions 
                          if t.timestamp <= end_date]
            
        return transactions


def run_demo():
    """Demonstrate BankAccount functionality with various scenarios."""
    print("Creating account with $100 initial balance...")
    account = BankAccount("12345", 100.0)
    print(f"Initial balance: ${account.balance:.2f}\n")
    
    # Demonstrate successful transactions
    print("Making some transactions...")
    try:
        account.deposit(50.0)
        print(f"After $50 deposit: ${account.balance:.2f}")
        account.withdraw(30.0)
        print(f"After $30 withdrawal: ${account.balance:.2f}")
    except (InvalidAmountError, InsufficientFundsError) as e:
        print(f"Error: {e}")
    
    # Demonstrate error handling
    print("\nTesting error conditions...")
    
    print("\nTrying to withdraw more than balance...")
    try:
        account.withdraw(1000.0)
    except InsufficientFundsError as e:
        print(f"✓ Caught expected error: {e}")
    
    print("\nTrying to deposit negative amount...")
    try:
        account.deposit(-50.0)
    except InvalidAmountError as e:
        print(f"✓ Caught expected error: {e}")
    
    # Show transaction history
    print("\nTransaction history:")
    for tx in account.get_statement():
        print(f"{tx.timestamp}: {tx.type.title():<10} ${tx.amount:>8.2f} "
              f"(Balance: ${tx.balance_after:.2f})")


if __name__ == "__main__":
    run_demo()
