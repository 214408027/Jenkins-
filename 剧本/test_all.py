import allure

class TestAllure:
    @allure.step(title = '前置')
    def setup(self):
        print('qianzhi ')

    @allure.step(title = '后置')
    def teardown(self):
        print('houzhi')
        
    @allure.step(title = '测试登录的流程')
    def test_login(self):
        print('呵呵哒')
        assert 1
        
    @allure.step(title = '测试退出的流程')
    def test_out(self):
        print('无敌了')
        assert 1
