import xlrd

# reading the excel file
workBook = xlrd.open_workbook("DataFile.xlsx")

# selecting the sheet
sheet = workBook.sheet_by_name("login")

# counting the row count
row_count = sheet.nrows
# counting the column
col_count = sheet.ncols

# reading the value from the excel
for row in range(1, row_count):
    UserName = sheet.cell_value(row, 0)
    Password = sheet.cell_value(row, 1)

    print(UserName)
    print(Password)
