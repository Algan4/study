from random import randint
from openpyxl import Workbook
print ('HI PEOPLE!')
columns_count = int(input('Введите ширину матрицы: '))
rows_count = int(input('Введите высоту матрицы: '))
#print(columns_count, rows_count)
#print(randint(1,100))
for colum in range(columns_count):
    for row in range(rows_count):
        print("\nТекущий столбик: ", colum)
        print("\nТекущая строка: ", row)

# создаем книгу
wb = Workbook()
# делаем единственный лист активным
ws = wb.active
ws.title = input("ВВедите название страницы: ")
for ws in wb:
    for colum in range(columns_count):
        for row in range(rows_count):
         ws.append(colum)

wb.save
