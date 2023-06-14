import pandas as pd

# Read the CSV file
data = pd.read_csv('AADB_dataset.csv')

# Drop duplicates based on the 'imgName' column
cleaned_data = data.drop_duplicates(subset=['imgName'], keep='first')

# Save cleaned data to a new CSV file
cleaned_data.to_csv('AADB_dataset.csv', index=False)

print("Data cleaning completed. Cleaned data saved to 'AADB_dataset.csv'.")