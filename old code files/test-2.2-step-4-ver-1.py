from selenium import webdriver
import time

##################### еще вариант с ActionChains
# driver = webdriver.Chrome()
# driver.get("https://SunInJuly.github.io/execute_script.html")
#
# try:
#     button = driver.find_element_by_tag_name("button")
#     time.sleep(1)
#     _ = button.location_once_scrolled_into_view
#
#     button.click()
#     assert True
# finally:
#   time.sleep(20)
#   driver.quit()

###############################
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# #button = browser.find_element_by_tag_name("button")
# #time.sleep(2)
# #browser.execute_script("window.scrollTo(0, 150)") # !!!!!!!!!!!!!!!!!!!!!! SCROOOOOOOOOOLLLLLLL
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()

from selenium import webdriver
browser = webdriver.Chrome()
browser2 = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
browser2.execute_script("document.title='Script executing';alert('ВТОРОЕ ОКНО БТЯЬ');")