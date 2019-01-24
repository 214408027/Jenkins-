import allure

class Test_allure:
    @allure.step(title = '前置')
    def setup(self):
        print('qianzhi ')

    @allure.step(title = '后置')
    def teardown(self):
        print('houzhi')



    @allure.step(title = '测试登录的流程')
    def test_login(self):

        allure.attach('登录', '呵呵哒')
        print('呵呵哒')

        assert 0
        
    def test_out(self):

    allure.attach('退出', '呵呵哒')
    print('无敌了')

    assert 1
