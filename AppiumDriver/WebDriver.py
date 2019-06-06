# __author__ = 'maocaiyuan'

import threading
from urllib.error import URLError
from appium import webdriver
from selenium.common.exceptions import WebDriverException
from Common import ReadConfig
import Common.Log as Log


class WebDriver:
    readConfigLocal = ReadConfig.ReadConfig()   # 读取配置文件
    driver = None
    log = Log.LogDriver.get_log()
    logger = log.get_logger()
    mutex = threading.Lock()

    platformName = readConfigLocal.get_config_value("platformName")     # 平台名字 iOS
    platformVersion = readConfigLocal.get_config_value("platformVersion")       # 平台版本 8.3...
    deviceName = readConfigLocal.get_config_value("deviceName")  # 设备名称
    bundleID = readConfigLocal.get_config_value("bundleID")     # bundleID
    app = readConfigLocal.get_config_value("app")
    automationName = readConfigLocal.get_config_value("automationName")
    UDID = readConfigLocal.get_config_value("UDID")
    newCommandTimeout = readConfigLocal.get_config_value("newCommandTimeout")
    platform = readConfigLocal.get_config_value("platform")

    command_executor = readConfigLocal.get_config_value("command_executor")     # appium执行地址
    desired_caps = {
                    "platformName": platformName,
                    "platformVersion": platformVersion,
                    "deviceName": deviceName,
                    "bundleId": bundleID,
                    "app": app,
                    "automationName": automationName,
                    "noReset": True,
                    "clearSystemFiles": True,
                    "noSign": True,
                    "udid": UDID,
                    "newCommandTimeout": newCommandTimeout,
                    "platform": platform}

    def _init__(self):
        pass

    @staticmethod  # 获取Appium Driver
    def get_driver():
        try:
            if not WebDriver.driver:
                WebDriver.mutex.acquire()   # 线程锁定
                if not WebDriver.driver:
                    try:
                        WebDriver.driver = webdriver.Remote(WebDriver.command_executor, WebDriver.desired_caps)
                        WebDriver.logger.info("打开驱动成功")
                    except URLError as e:
                        WebDriver.driver = None
                        WebDriver.logger.info("打开驱动失败")
                        # print(e)

                WebDriver.mutex.release()   # 线程释放

        except WebDriverException:
            WebDriver.logger.info("无法打开驱动")
            raise

        return WebDriver.driver
