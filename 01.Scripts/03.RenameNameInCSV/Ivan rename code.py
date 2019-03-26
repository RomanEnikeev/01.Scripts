import xlrd
rb = xlrd.open_workbook('C:/Users/r.enikeev/pythochik/final.xlsx',formatting_info=True)
Ksheet = rb.sheet_by_index(0)
Kfor rownum in range(sheet.nrows):
K    row = sheet.row_values(rownum)
Kfor c_el in row:
K    print(c_el)
K