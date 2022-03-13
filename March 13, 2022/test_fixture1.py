from selenium import webdriver
from os import system

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():#этот код открывает браузер один раз в начале и в конце теста

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite.. 1")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #browser = webdriver.Chrome(executable_path='<path-to-chrome>', options=options)
        self.browser = webdriver.Chrome(options=options)
        #self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite.. 1")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2(): #этот код открывает браузер два раза

    def setup_method(self):
        print("\nstart browser for test.. 2")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test.. 2")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# def main():
#     system(f'pytest -s "{__file__}"')
# if __name__ == "__main__":
#     main()


# мой вариант 3

# class TestMainPage3(): #этот код открывает браузер один раз и содержит два теста в одном
#                        #но лучше так не делать, лучше один тест в одной проверке
#
#     def setup_method(self):
#         print("start browser for test..")
#         self.browser = webdriver.Chrome()
#
#     def teardown_method(self):
#         print("quit browser for test..")
#         self.browser.quit()
#
#     def test_guest_should_see_login_link_and_basket_link(self):
#         self.browser.get(link)
#         self.browser.find_element_by_css_selector("#login_link")
#         print("Test 1 - OK")
#         self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
#         print("Test 2 - OK")

    # def test_guest_should_see_basket_link_on_the_main_page(self):
    #     self.browser.get(link)
    #     self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

#pytest test_fixture1.py