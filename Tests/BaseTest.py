import unittest
from selenium import webdriver


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="F:/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://www.flickr.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Complete")
