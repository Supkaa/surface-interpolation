import os

import numpy as np
import xlrd


class DataExcel:
    def __init__(self, url: str):
        self.url = url
        self._loadData()

    # def _loadData(self):
    #     workbook = xlrd.open_workbook(self.url)
    #     worksheet = workbook.sheet_by_index(0)

    #     self.x = np.array(worksheet.col_values(2, 4), dtype=float)
    #     self.y = np.array(worksheet.col_values(1, 4), dtype=float)
    #     self.z = np.array(worksheet.col_values(5, 4), dtype=float)

    #     print(f'[INFO] Load complete')

    def _loadData(self):
        workbook = xlrd.open_workbook(self.url)
        worksheet = workbook.sheet_by_index(0)
        
        dat = {}

        for i in range(worksheet.nrows):
            for j in range(worksheet.ncols):
                if worksheet.cell_value(i,j) == 'X':
                    dat['X'] = j, i+1
                if worksheet.cell_value(i,j) == 'Y':
                    dat['Y'] = j, i+1
                if (cx := worksheet.cell_value(i,j)) == 'Z' or cx == 'Глубина кровли     пласта "а",м':
                    dat['Z'] = j, (i+1 if worksheet.cell_value(i+1,j) != '' else i+2)

        self.x = np.array(worksheet.col_values(*dat['X']), dtype=float)
        self.y = np.array(worksheet.col_values(*dat['Y']), dtype=float)
        self.z = np.array(worksheet.col_values(*dat['Z']), dtype=float)
