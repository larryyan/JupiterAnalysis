import xlrd

data = xlrd.open_workbook('excel/test.xlsx')
table = data.sheets()[0]          #通过索引顺序获取

TimeRow = table.row_values(0, start_colx= 1)
OneRow = table.row_values(1, start_colx= 1)
TwoRow = table.row_values(2, start_colx= 1)
ThreeRow = table.row_values(3, start_colx= 1)
FourRow = table.row_values(4, start_colx= 1)

print(TimeRow)
print(OneRow)
print(TwoRow)
print(ThreeRow)
print(FourRow)