import os

import numpy as np
import xlrd


class DataExcel:
    def __init__(self, url: str):
        self.url = url
        self._loadData()

    def _loadData(self):
        workbook = xlrd.open_workbook(self.url)
        worksheet = workbook.sheet_by_index(0)

        self.x = np.array(worksheet.col_values(2, 4), dtype=float)
        self.y = np.array(worksheet.col_values(1, 4), dtype=float)
        self.z = np.array(worksheet.col_values(5, 4), dtype=float)

        print(f'[INFO] Load complete')
