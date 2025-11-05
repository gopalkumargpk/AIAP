import pandas as pd
from typing import Dict, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime
import json
import logging
from pathlib import Path

@dataclass
class LoanApplication:
    application_id: str
    timestamp: datetime
    # Personal Information
    full_name: str
    age: int
    # Financial Information
    annual_income: float
    employment_years: float
    credit_score: int
    existing_debt: float
    loan_amount: float
    loan_purpose: str
    # Optional collateral
    collateral_value: Optional[float] = None
    
    def to_dict(self) -> Dict:
        """Convert application to dictionary for storage"""
        return {
            'application_id': self.application_id,
            'timestamp': self.timestamp.isoformat(),
            'full_name': self.full_name,
            'age': self.age,
            'annual_income': self.annual_income,
            'employment_years': self.employment_years,
            'credit_score': self.credit_score,
            'existing_debt': self.existing_debt,
            'loan_amount': self.loan_amount,
            'loan_purpose': self.loan_purpose,
            'collateral_value': self.collateral_value
        }

class LoanApprovalSystem:
    def __init__(self):
        self.setup_logging()
        self.load_config()
        
    def setup_logging(self):
        """Setup logging for audit trail"""
        logging.basicConfig(
            filename='loan_approval_audit.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
    
    def load_config(self):
        """Load configuration parameters"""
        self.config = {
            'min_credit_score': 600,
            'max_dti_ratio': 0.43,  # Debt-to-Income ratio
            'min_employment_years': 1.0,
            'min_age': 18,
            'income_to_loan_ratio': 3,  # Annual income should be at least 3x loan amount
        }
    
    def calculate_risk_score(self, application: LoanApplication) -> float:
        """
        Calculate risk score based on objective financial criteria only
        Returns a score between 0 and 100 (higher is better)
        """
        # Base score from credit score (max 40 points)
        credit_score_points = min(40, (application.credit_score - 300) / 5)
        
        # Debt-to-Income ratio (max 20 points)
        monthly_debt = application.existing_debt / 12
        monthly_income = application.annual_income / 12
        dti_ratio = (monthly_debt + (application.loan_amount / 12)) / monthly_income
        dti_points = max(0, 20 * (1 - dti_ratio / self.config['max_dti_ratio']))
        
        # Employment stability (max 20 points)
        employment_points = min(20, application.employment_years * 4)
        
        # Loan amount to income ratio (max 20 points)
        income_ratio = application.annual_income / application.loan_amount
        income_points = min(20, income_ratio * 20 / self.config['income_to_loan_ratio'])
        
        # Calculate total score
        total_score = credit_score_points + dti_points + employment_points + income_points
        
        # Log the scoring breakdown for transparency
        logging.info(f"Application {application.application_id} scoring breakdown:")
        logging.info(f"Credit Score Points: {credit_score_points:.2f}")
        logging.info(f"DTI Points: {dti_points:.2f}")
        logging.info(f"Employment Points: {employment_points:.2f}")
        logging.info(f"Income Ratio Points: {income_points:.2f}")
        logging.info(f"Total Score: {total_score:.2f}")
        
        return total_score
    
    def evaluate_application(self, application: LoanApplication) -> Tuple[bool, str, float]:
        """
        Evaluate a loan application based on objective criteria only
        Returns: (approved, reason, risk_score)
        """
        try:
            # Log application receipt
            logging.info(f"Evaluating application {application.application_id}")
            
            # Basic eligibility checks
            if application.age < self.config['min_age']:
                return False, "Applicant must be at least 18 years old.", 0
                
            if application.credit_score < self.config['min_credit_score']:
                return False, "Credit score below minimum requirement.", 0
                
            if application.employment_years < self.config['min_employment_years']:
                return False, "Minimum employment history not met.", 0
            
            # Calculate debt-to-income ratio
            monthly_debt = application.existing_debt / 12
            monthly_income = application.annual_income / 12
            new_monthly_payment = application.loan_amount / 12  # Simplified calculation
            dti_ratio = (monthly_debt + new_monthly_payment) / monthly_income
            
            if dti_ratio > self.config['max_dti_ratio']:
                return False, "Debt-to-income ratio too high.", 0
            
            # Calculate risk score
            risk_score = self.calculate_risk_score(application)
            
            # Approval thresholds
            if risk_score >= 80:
                decision = True
                reason = "Application approved - Excellent qualification"
            elif risk_score >= 70:
                decision = True
                reason = "Application approved - Good qualification"
            elif risk_score >= 60:
                if application.collateral_value and application.collateral_value >= application.loan_amount:
                    decision = True
                    reason = "Application approved with collateral"
                else:
                    decision = False
                    reason = "Application denied - Insufficient qualification"
            else:
                decision = False
                reason = "Application denied - Does not meet minimum criteria"
            
            # Log decision
            logging.info(f"Application {application.application_id} - Decision: {decision}, "
                        f"Risk Score: {risk_score:.2f}, Reason: {reason}")
            
            return decision, reason, risk_score
            
        except Exception as e:
            logging.error(f"Error processing application {application.application_id}: {str(e)}")
            raise
    
    def save_application(self, application: LoanApplication, decision: bool, 
                        reason: str, risk_score: float):
        """Save application and decision for audit purposes"""
        result = {
            **application.to_dict(),
            'decision': decision,
            'reason': reason,
            'risk_score': risk_score
        }
        
        # Save to JSON file
        history_file = Path('loan_history.json')
        if history_file.exists():
            with open(history_file, 'r') as f:
                history = json.load(f)
        else:
            history = []
            
        history.append(result)
        
        with open(history_file, 'w') as f:
            json.dump(history, f, indent=2)
            
        logging.info(f"Application {application.application_id} saved to history")

def test_loan_system():
    """Test the loan approval system with various scenarios"""
    system = LoanApprovalSystem()
    
    # Test cases with different demographics but similar financial profiles
    test_cases = [
        {
            'application_id': 'APP001',
            'full_name': 'Sarah Johnson',
            'age': 35,
            'annual_income': 75000,
            'employment_years': 5,
            'credit_score': 720,
            'existing_debt': 15000,
            'loan_amount': 200000,
            'loan_purpose': 'Home Purchase'
        },
        {
            'application_id': 'APP002',
            'full_name': 'Michael Chen',
            'age': 35,
            'annual_income': 75000,
            'employment_years': 5,
            'credit_score': 720,
            'existing_debt': 15000,
            'loan_amount': 200000,
            'loan_purpose': 'Home Purchase'
        },
        {
            'application_id': 'APP003',
            'full_name': 'Maria Garcia',
            'age': 35,
            'annual_income': 75000,
            'employment_years': 5,
            'credit_score': 720,
            'existing_debt': 15000,
            'loan_amount': 200000,
            'loan_purpose': 'Home Purchase'
        }
    ]
    
    print("\nTesting Loan Approval System for Bias\n")
    print("Using identical financial profiles with different applicant names:")
    
    results = []
    for case in test_cases:
        application = LoanApplication(
            timestamp=datetime.now(),
            **case
        )
        
        decision, reason, risk_score = system.evaluate_application(application)
        system.save_application(application, decision, reason, risk_score)
        
        results.append({
            'name': case['full_name'],
            'decision': decision,
            'risk_score': risk_score,
            'reason': reason
        })
    
    # Display results
    print("\nResults:")
    print("-" * 80)
    for result in results:
        print(f"Applicant: {result['name']}")
        print(f"Decision: {'Approved' if result['decision'] else 'Denied'}")
        print(f"Risk Score: {result['risk_score']:.2f}")
        print(f"Reason: {result['reason']}")
        print("-" * 80)
    
    # Analyze for bias
    risk_scores = [r['risk_score'] for r in results]
    if len(set(risk_scores)) == 1:
        print("\nBias Analysis: PASS ✅")
        print("All applications with identical financial profiles received the same risk score.")
    else:
        print("\nBias Analysis: FAIL ❌")
        print("Inconsistent risk scores detected for identical financial profiles.")

if __name__ == "__main__":
    test_loan_system()