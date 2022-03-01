from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    #browser.find_element_by_xpath(".//*[@placeholder = 'Введите имя']").send_keys("Иван")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("BILL")

    #browser.find_element_by_xpath(".//*[@placeholder = 'Введите фамилию']").send_keys("Иванов")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("GATES")

    #browser.find_element_by_xpath(".//*[@placeholder = 'Введите Email']").send_keys("ivan@yandex.ru")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("BILL_GATES@WINDOWS.COM")

    #browser.find_element_by_css_selector("button.btn").click()
    browser.find_element(By.XPATH, "//*[text()='Submit']").click()

    time.sleep(1)
    #return browser.find_element_by_tag_name("h1").text
    return browser.find_element(By.TAG_NAME, "h1").text

class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),"Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

if __name__ == "__main__":
    unittest.main()