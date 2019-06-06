from Fixture.FixtureBase import *


@pytest.mark.usefixtures("setup_class")
class TestLogin:

    @pytest.mark.website
    def test_1(self, setup_function):
        print('Test_1 called.')

    def test_2(self, setup_module):
        print('Test_2 called.')

    def test_3(self, setup_module):
        print('Test_3 called.')
        assert 2 == 1+1              # 通过assert断言确认测试结果是否符合预期
