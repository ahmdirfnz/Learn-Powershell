import pandas as pd

# Read the Excel file and access the sheets
excel_file = pd.ExcelFile('Email Support Update Copy.xlsx')
table1 = pd.read_excel(excel_file, sheet_name =  'Table1')
table2 = pd.read_excel(excel_file, sheet_name =  'Table2')

# Merge the two tables based on their corresponding ID
merged_table = pd.merge(table1, table2, on='CI Name')

# Iterate over each row in the merged table
for index, row in merged_table.iterrows():
    # Compare the values of each column
    if row['Column1_x'] == row['Column1_y']:
        print('Values in Column1 match for CI Name:', row['CI Name'])
    else:
        print('Values in Column1 do not match for CI Name:', row['CI Name'])
    
    if row['Column2_x'] == row['Column2_y']:
        print('Values in Column2 match for CI Name:', row['CI Name'])
    else:
        print('Values in Column2 do not match for CI Name:', row['CI Name'])

    # Add more columns to compare as needed