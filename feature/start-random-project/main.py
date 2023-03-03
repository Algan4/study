import csv
import random
from random import randint
import numpy as np
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.utils import column_index_from_string
import pandas as pd

print ('HI PEOPLE!')
columns_count = int(input('Введите ширину матрицы: '))
rows_count = int(input('Введите высоту матрицы: '))
mas = np.random.randint(100, size=(columns_count, rows_count))
print(mas)
# создаем книгу
wb = Workbook()
# делаем единственный лист активным
ws = wb.active
df = pd.DataFrame(mas)
df.to_excel (r'C:\Test\1\mydata.xlsx')
#np.savetxt (" my_data.csv", mas, delimiter="\t" , fmt=" %.2f ")
#for colum in range(columns_count):
#    for row in range(rows_count):
#        print("\nТекущий столбик: ", colum)
#        print("\nТекущая строка: ", row)

#ws.append(mas)
#ws.title = input("ВВедите название страницы: ")
#wb.save(filename="sample.xls")
