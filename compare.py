import csv
import openpyxl

csvfile1 = 'date1.csv'
csvfile2 = 'date2.csv'

data1 = []
data2 = []
data3 = []

with open(csvfile1, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        data1.append(row[0])  # Assuming there's only one column

with open(csvfile2, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        data2.append(row[0])  # Assuming there's only one column

for item in data1:
    if item not in data2:
        data3.append(item)

workbook = openpyxl.Workbook()
worksheet = workbook.active

for item in data3:
    worksheet.append([item])

excel_file = 'output.xlsx'
workbook.save(excel_file)

print(f'Data from data3 has been written to {excel_file}.')