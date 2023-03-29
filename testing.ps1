# Install the Import-Excel module if you haven't already
Install-Module Import-Excels

# Import the Excel file
$excel_file = 'example.xlsx'
$data = Import-Excel $excel_file

# Select the column you want to extract
$column_name = 'column_name'
$column = $data.$column_name

# Convert the column to a list
$values = @($column)

# Print the list of values
Write-Output $values