import pandas as pd

def analyze_csv(file_path):
    # Read the CSV file
    try:
        df = pd.read_csv(file_path)
        
        # Get numeric columns only
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        
        # Calculate statistics for each numeric column
        for column in numeric_cols:
            print(f"\nStatistics for {column}:")
            print(f"Mean: {df[column].mean():.2f}")
            print(f"Minimum: {df[column].min():.2f}")
            print(f"Maximum: {df[column].max():.2f}")
            print("-" * 30)
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
# analyze_csv('your_file.csv')