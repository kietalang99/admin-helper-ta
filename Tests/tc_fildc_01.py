from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import Select
from Pages.loginPage import LoginPage

class filterByDeviceCategory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Admin/PycharmProjects/admin/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("https://admin-helper-f21c1.web.app/login")
        login = LoginPage(driver)
        login.enter_email("admin@gmail.com")
        login.enter_password("123456")
        login.click_login()
        cls.driver.implicitly_wait(10)

    def test_filter_device_category_02(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[2]/a').click()
        select = Select(self.driver.find_element_by_id("device-category"))
        select.select_by_index(0);
        select.select_by_value("1");
        select.select_by_visible_text(" Phone ");

        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test filter by Laptop category was completed")
