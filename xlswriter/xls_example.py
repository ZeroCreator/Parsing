import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx') # Создать файл
worksheet = workbook.add_worksheet() # Создать лист, вы можете указать имя листа с помощью work.add_worksheet ('employee'), но китайское имя будет сообщать об ошибке UnicodeDecodeErro
worksheet.write('A1', 'Hello world') # Написать в A1
workbook.close()