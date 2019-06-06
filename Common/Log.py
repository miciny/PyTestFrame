import logging
import os
import threading
import time
from time import sleep
from Common import ReadConfig


class Log:

    def __init__(self):
        global logger, resultPath, logPath
        resultPath = os.path.join(ReadConfig.prj_dir, "../Result")  # 执行结果路径
        logPath = os.path.join(resultPath, (time.strftime('%Y%m%d%H%M%S', time.localtime())))  # 执行日志路径

        if not os.path.exists(logPath):  # 如果没有,创建log路径
            os.makedirs(logPath)
        self.checkNo = 0  # 执行时出错的检查编号
        self.logger = logging.getLogger()  # logger
        self.logger.setLevel(logging.INFO)

        fh = logging.FileHandler(os.path.join(logPath, "outPut.log"), encoding="UTF-8")  # 日志输出到文件
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 日志输出到文件的格式
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    @staticmethod  # 静态方法,不必传入self,获取结果目录
    def get_result_path():
        report_path = os.path.join(logPath, "report.html")
        return report_path

    # 返回logger
    def get_logger(self):
        return self.logger

    # 画开始线,outPut.log
    def build_start_line(self, case_no):
        start_line = "----  " + case_no + "   " + "START" + "   " + "  ----"
        self.logger.info(start_line)

    # 画结束线
    def build_end_line(self, case_no):
        end_line = "----  " + case_no + "   " + "END" + "   " + "  ----"
        self.logger.info(end_line)
        self.checkNo = 0

    # 写结果 OK或者NG, 写入到report.text
    def write_result(self, result):
        report_path = os.path.join(logPath, "report.txt")
        flogging = open(report_path, "a")
        try:
            flogging.write(result+"\n")
        finally:
            flogging.close()
        pass

    # 写入结果OK
    def result_ok(self, case_no):
        self.write_result(case_no+": OK")

    # 写入结果NG
    def result_ng(self, case_no):
        self.write_result(case_no+": NG")

    # 写入检查点OK
    def check_point_ok(self, driver, case_name, check_point):
        self.checkNo += 1
        self.logger.info("[CheckPoint_"+str(self.checkNo)+"]: "+check_point+": OK")
        # 截屏
        self.screenshot_ok(driver, case_name)

    # 写入检查点NG
    def check_point_ng(self, driver, case_name, check_point):
        self.checkNo += 1
        self.logger.info("[CheckPoint_"+str(self.checkNo)+"]: "+check_point+": NG")
        # 截屏
        self.screenshot_ng(driver, case_name)

    # 截屏 OK
    def screenshot_ok(self, driver, case_name):
        screenshot_path = os.path.join(logPath, case_name)
        screenshot_name = "CheckPoint_"+str(self.checkNo)+"_OK.png"

        # 截屏之前,等待动画完成
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshot_path, screenshot_name))

    # 截屏 NG
    def screenshot_ng(self, driver, case_name):
        screenshot_path = os.path.join(logPath)
        screenshot_name = "CheckPoint_"+str(self.checkNo)+"_NG.png"

        # 截屏之前,等待动画完成
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshot_path, screenshot_name))

    # 截屏错误
    def screenshot_error(self, driver, case_name):
        screenshot_path = os.path.join(logPath, case_name)
        screenshot_name = "ERROR.png"

        # 截屏之前,等待动画完成
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshot_path, screenshot_name))


class LogDriver:
    """
    用于获取Log,单例控制?
    """
    log = Log()
    mutex = threading.Lock()  # 线程锁,控制对共享资源的访问

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if not LogDriver.log:
            LogDriver.mutex.acquire()
            LogDriver.log = Log()
            LogDriver.mutex.release()
        return LogDriver.log


if __name__ == "__main__":
    log_test = LogDriver.get_log()
    logger = log_test.get_logger()
    logger.debug("1111")
    log_test.build_start_line("test")
