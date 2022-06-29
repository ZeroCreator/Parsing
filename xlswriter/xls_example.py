import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx') # Создать файл
worksheet = workbook.add_worksheet() # Создать лист, вы можете указать имя листа с помощью work.add_worksheet ('employee'), но китайское имя будет сообщать об ошибке UnicodeDecodeErro
worksheet.write('A1', 'Hello world') # Написать в A1
workbook.close()

# расчет формулы в Excel
# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],
)

# Начать с первой ячейки. Строки и столбцы индексируются нулем. Запись по метке начинается с 0, а запись по абсолютной позиции "A1" начинается с 1
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')  # Вызываем формульное выражение excel

workbook.close()

