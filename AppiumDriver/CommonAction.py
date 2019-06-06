# __author__ = 'maocaiyuan'

from AppiumDriver.WebDriver import WebDriver


def get_window_size():
    """
    获取当前屏幕大小
    :return:windowSize
    """
    # 全局变量 后面要用到屏幕的长宽
    global windowSize
    global width
    global height

    driver = WebDriver.get_driver()
    windowSize = driver.get_window_size()
    width = windowSize.get("width")
    height = windowSize.get("height")

    return windowSize


def get_current_activity():
    """
    获取当前窗口名词(仅安卓)
    :return:
    """
    driver = WebDriver.get_driver()
    return driver.current_activity()


def swipe_up(during=None):
    """
    往上滑
    :param during: 最好挺大的,不然滑不动
    :return:
    """
    get_window_size()
    driver = WebDriver.get_driver()
    driver.swipe(width/2, height*3/4, width/2, height/4, during)


def swipe_down(during=None):
    """
    往下滑
    :param during:
    :return:
    """
    get_window_size()
    driver = WebDriver.get_driver()
    driver.swipe(width/2, height/4, width/2, height*3/4, during)


def swipe_left(during=None):
    """
    往右滑
    :param during:
    :return:
    """
    get_window_size()
    driver = WebDriver.get_driver()
    driver.swipe(width/4, height/2, width*3/4, height/2, during)


def swipe_right(during=None):
    """
    往左滑
    :param during:
    :return:
    """
    get_window_size()
    driver = WebDriver.get_driver()
    driver.swipe(width*4/5, height/2, width/5, height/2, during)


def hide_keyboard(key_name=None, key=None, strategy=None):
    """
    隐藏键盘,如果不行,只能点done隐藏,strategy HideKeyBoardStrategy.PRESS_KEY,'Done'
    :param key_name:
    :param key:
    :param strategy: strategy='tapOutside'
    :return:
    """
    driver = WebDriver.get_driver()
    driver.hide_keyboard(key_name, key, strategy)


# App安装与卸载类API
def is_app_installed(bundle_id):
    """
    根据bundleId来判断该应用是否已经安装
    :param bundle_id:
    :return:
    """
    driver = WebDriver.get_driver()
    return driver.is_app_installed(bundle_id)


def close_app():
    """
    关闭应用，其实就是按home键把应用置于后台
    :return:
    """
    driver = WebDriver.get_driver()
    driver.close_app()


def launch_app():
    """
    启动应用
    :return:
    """
    driver = WebDriver.get_driver()
    driver.launch_app()


def reset_app():
    """
    先closeApp然后在launchAPP
    :return:
    """
    driver = WebDriver.get_driver()
    driver.reset()
