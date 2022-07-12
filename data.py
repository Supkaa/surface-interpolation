import numpy as np
import xlrd

class DataExcel:
     def __init__(self):
          self._loadData()

     def _loadData(self):
          url = input('Перетащите файл в консоль -> ')
          workbook = xlrd.open_workbook(f'{url}')
          worksheet = workbook.sheet_by_index(0)

          self.x = np.array(worksheet.col_values(2, 4), dtype=float)
          self.y = np.array(worksheet.col_values(1, 4), dtype=float)
          self.z = np.array(worksheet.col_values(5, 4), dtype=float)

          print(f'[INFO] Load complete')

