import pytest
from AppiumDriver.CommonAction import *
from AppiumDriver import AppiumServer
import Common.Log as Log


# 每个test调用一次
@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called.")
        # reset_app()
    request.addfinalizer(teardown_function)
    print('setup_function called.')
    # reset_app()


# 多个test，调用一次，使用同一参数
@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        print("teardown_module called.")
        # reset_app()
    request.addfinalizer(teardown_module)
    print('setup_module called.')
    # reset_app()


# 每个class用一次
@pytest.fixture(scope='class')
def setup_class(request):
    def teardown_module():
        print("teardown_class called.")
        # reset_app()
        log.build_end_line("123321")
    request.addfinalizer(teardown_module)
    print('setup_class called.')
    # reset_app()
    log = Log.LogDriver.get_log()
    log.build_start_line("123321")


# 每个session用一次，如启动服务
@pytest.fixture(scope='session')
def setup_session(request):
    def teardown_module():
        print("teardown_session called.")
        server.stop_server()
    request.addfinalizer(teardown_module)
    print('setup_session called.')
    server = AppiumServer.AppiumServer()
    server.start_server()
