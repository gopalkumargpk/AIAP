# TGNPDCL Electricity Bill Calculator

def calculate_electricity_bill(units, customer_type):
    # Initialize charges
    ec = 0  # Energy Charges
    fc = 0  # Fixed Charges
    cc = 0  # Customer Charges
    ed = 0  # Electricity Duty
    
    # Set rates based on customer type
    if customer_type.lower() == 'domestic':
        # Example rates for domestic customers
        if units <= 100:
            rate = 3.50
        elif units <= 200:
            rate = 4.50
        else:
            rate = 6.00
        fc = 50  # Fixed charge for domestic
        cc = 25  # Customer charge for domestic
        ed_percentage = 6  # 6% of EC for domestic
        
    elif customer_type.lower() == 'commercial':
        # Example rates for commercial customers
        if units <= 100:
            rate = 6.50
        elif units <= 200:
            rate = 7.50
        else:
            rate = 9.00
        fc = 100  # Fixed charge for commercial
        cc = 50   # Customer charge for commercial
        ed_percentage = 8  # 8% of EC for commercial
        
    else:
        return "Invalid customer type"
    
    # Calculate charges
    ec = units * rate
    ed = (ec * ed_percentage) / 100
    total_bill = ec + fc + cc + ed
    
    return {
        'EC': ec,
        'FC': fc,
        'CC': cc,
        'ED': ed,
        'Total': total_bill
    }

def main():
    print("TGNPDCL Electricity Bill Calculator")
    print("-" * 35)
    
    # Get input from user
    try:
        units = float(input("Enter the number of units consumed: "))
        customer_type = input("Enter customer type (Domestic/Commercial): ")
        
        # Calculate bill
        bill = calculate_electricity_bill(units, customer_type)
        
        if isinstance(bill, str):
            print(bill)
        else:
            print("\nBill Details:")
            print("-" * 20)
            print(f"Energy Charges    : ₹{bill['EC']:.2f}")
            print(f"Fixed Charges     : ₹{bill['FC']:.2f}")
            print(f"Customer Charges  : ₹{bill['CC']:.2f}")
            print(f"Electricity Duty  : ₹{bill['ED']:.2f}")
            print("-" * 20)
            print(f"Total Bill Amount : ₹{bill['Total']:.2f}")
            
    except ValueError:
        print("Please enter a valid number for units")

if __name__ == "__main__":
    main()
