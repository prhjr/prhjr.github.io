import pandas as pd

# Define the column names
fein_column = 'FEIN'  # Change this to the name of your FEIN column
client_name_column = 'Client Name'  # Change this to the name of your Client Name column

# Load the Excel file
file_path = '/Users/pjhughes/Desktop/Current/IES3.20.24.xlsx'  # Change this to the path of your Excel file
df = pd.read_excel(file_path)

# Check for duplicate FEINs with different Client Names
fein_duplicates = df[df.duplicated(fein_column, keep=False)]
fein_issues = fein_duplicates[fein_duplicates.duplicated(client_name_column, keep='first') == False]

# Check for duplicate Client Names with different FEINs
client_name_duplicates = df[df.duplicated(client_name_column, keep=False)]
client_name_issues = client_name_duplicates[client_name_duplicates.duplicated(fein_column, keep='first') == False]

# Combine the issues
issues = pd.concat([fein_issues, client_name_issues]).drop_duplicates()

# Print the issues
if not issues.empty:
    print("The following rows have issues:")
    print(issues)
else:
    print("No issues found.")