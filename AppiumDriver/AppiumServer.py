# __author__ = 'maocaiyuan'

import os
import threading
import urllib.request
from multiprocessing import Process
from time import sleep
from urllib.error import URLError
from Common import ReadConfig
import Common.Log as Log

readConfigLocal = ReadConfig.ReadConfig()


class AppiumServer:

    def __init__(self):
        global udid, bundleId, command_executor, logger
        udid = readConfigLocal.get_config_value("udid")
        bundleId = readConfigLocal.get_config_value("bundleId")
        command_executor = readConfigLocal.get_config_value("command_executor")
        log = Log.LogDriver.get_log()
        logger = log.get_logger()

    def start_server(self):
        """
        启动服务
        :return:
        """
        if self.is_running():
            logger.info("Appium服务已开启")
        else:
            start_command = "appium"
            t1 = RunServer(start_command)
            p = Process(target=t1.start())  # 用进程启动服务,不会出现启动服务后,终端不接受其他命令的问题
            p.start()

    def stop_server(self):
        """
        关闭服务
        :return:
        """
        # kill myServer
        if self.is_running():
            killnode = "killall node"
            os.popen(killnode)
        else:
            print("Appium服务没有开启，无法关闭")

    def restart_server(self):
        """
        重启服务
        :arg:
        :return:
        """
        self.stop_server()
        self.start_server()

    @staticmethod
    def is_running():
        """
        服务是否启动了,URL打开,结果是2开头的就表示已启动
        :return:True or False
        """
        response = None
        url = command_executor+"/status"
        try:
            response = urllib.request.urlopen(url, timeout=5)
            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()


class RunServer(threading.Thread):
    """
    用进程启动服务,不会出现启动服务后,终端不接受其他命令的问题
    """

    def __init__(self, terminal):
        threading.Thread.__init__(self)
        self.terminal = terminal

    def run(self):
        os.system(self.terminal)


if __name__ == "__main__":
    oo = AppiumServer()
    oo.start_server()
    sleep(5)
    oo.stop_server()
