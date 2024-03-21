import pandas as pd

# Define the column names
fein_column = 'FEIN'
client_name_column = 'Client ID'

# Load the Excel file
file_path = '/Users/pjhughes/Desktop/Current/IES3.20.24.xlsx'
df = pd.read_excel(file_path)

# Convert FEIN and Client Name columns to strings
df[fein_column] = df[fein_column].astype(str)
df[client_name_column] = df[client_name_column].astype(str)

# Find FEINs with multiple Client Names
fein_issues = df.groupby(fein_column)[client_name_column].nunique()
fein_issues = fein_issues[fein_issues > 1].index.tolist()
fein_issues_table = df[df[fein_column].isin(fein_issues)].sort_values(by=fein_column)

# Find Client Names with multiple FEINs
client_name_issues = df.groupby(client_name_column)[fein_column].nunique()
client_name_issues = client_name_issues[client_name_issues > 1].index.tolist()
client_name_issues_table = df[df[client_name_column].isin(client_name_issues)].sort_values(by=client_name_column)

# Export the issues tables to an Excel file
with pd.ExcelWriter('issues_summary.xlsx') as writer:
    fein_issues_table.to_excel(writer, sheet_name='FEIN Issues', index=False)
    client_name_issues_table.to_excel(writer, sheet_name='Client Name Issues', index=False)

print("Issues summary exported to 'issues_summary.xlsx'.")