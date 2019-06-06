import os
import xlrd  # 倒入excel模块
from Common import ReadConfig


# excel
def get_xls(sheet_name, xlsx_name):
    """
    获取excel的值
    :param sheet_name
    :param xlsx_name
    :return:cls
    """

    xls_path = os.path.join(ReadConfig.prj_dir, "Elements", xlsx_name)
    # index = 0
    # read the excel
    data = xlrd.open_workbook(xls_path)

    # get the sheet
    table = data.sheet_by_name(sheet_name)  # 表名
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数

    cls = [["" for _ in range(ncols)] for _ in range(nrows-1)]
    for i in range(nrows-1):
        for j in range(ncols):
            cls[i][j] = str(table.row_values(i+1)[j])
    return cls


if __name__ == "__main__":
    print(get_xls("login", "TestCase.xlsx"))
