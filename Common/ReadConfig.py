# __author__ = 'Maocaiyuan'

import os
import codecs
import configparser

# 读写配置文件
# -read(filename) 直接读取ini文件内容
# -sections() 得到所有的section，并以列表的形式返回
# -options(section) 得到该section的所有option
# -items(section) 得到该section的所有键值对
# -get(section,option) 得到section中option的值，返回为string类型
# 获取配置文件里的常量的函数


prj_dir = os.path.split(os.path.realpath(__file__))[0]
configfile_path = os.path.join(prj_dir, "../Config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configfile_path, encoding="UTF-8")
        data = fd.read()
        # remove BOM 在windows上使用open打开utf-8编码的txt文件时开头会有一个多余的字符,它叫BOM,
        # 是用来声明编码等信息的,但python会把它当作文本解析
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configfile_path, "w")
            file.write(data)
            file.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(configfile_path, encoding="UTF-8")

    # name为配置文件里的常量名称
    def get_config_value(self, name):
        value = self.cf.get("config", name)
        return value
