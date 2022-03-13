import time
import math
import pytest
from selenium import webdriver


url_list = ['https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236896/step/1',
            'https://stepik.org/lesson/236897/step/1',
            'https://stepik.org/lesson/236898/step/1',
            'https://stepik.org/lesson/236899/step/1',
            'https://stepik.org/lesson/236903/step/1',
            'https://stepik.org/lesson/236904/step/1',
            'https://stepik.org/lesson/236905/step/1']


class TestFindCode():

    @pytest.fixture(scope='function')
    def driver(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()

    @pytest.mark.parametrize('url', url_list)
    def test_find_code(self, driver, url):
        driver.get(url)
        driver.find_element_by_css_selector('textarea.textarea').send_keys(str(math.log(int(time.time()))))
        driver.find_element_by_css_selector('button.submit-submission').click()
        feedback = driver.find_element_by_css_selector('pre.smart-hints__hint').text
        assert feedback == 'Correct!', 'This is part of alient message: ' + feedback