import xlsxwriter  # Строить документы и листы.

workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet()  # Добавьте полужирный формат для выделения ячеек. Установите полужирный шрифт, по умолчанию - False.
bold = workbook.add_format({'bold': True})  # Добавить числовой формат для ячеек с деньгами. Определить числовой формат
money = workbook.add_format({
                                'num_format': '$#,##0'})  # Напишите несколько заголовков данных. Напишите заголовок в произвольном полужирном формате blod
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)  # Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50],
)  # Start from the first cell below the headers.
row = 1
col = 0  # Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col, item)  # Пишите в формате по умолчанию
    worksheet.write(row, col + 1, cost, money)  # Пишите в произвольном денежном формате
    row += 1  # Write a total using a formula.
worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)

workbook.close()
# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')  # Вызываем формульное выражение excel

workbook.close()