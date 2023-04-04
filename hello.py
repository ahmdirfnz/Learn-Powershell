import pandas as pd
import json

# read Excel file into a pandas DataFrame
df = pd.read_excel('excel playground.xlsx')

# convert DataFrame to JSON
json_str = df.to_json(orient='records')

# print the JSON string
print(json_str)