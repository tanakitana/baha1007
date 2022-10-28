import time

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestMePlease(unittest.TestCase):

    def setUp(self) -> None:
        # initialisation
        self.driver = webdriver.Edge()
        self.driver.set_window_size(1024, 768)

    def test_1(self):
        """user able navigate to documentation
            section via clicking Documentation link"""
        self.driver.get('https://www.selenium.dev/about/')  #hey, we go there
        doc_link = self.driver.find_element(By.CSS_SRLECTOR, "a[href='/documntation']")
        doc_link.click()
        self.assertEqual(self.driver.title, "The Selenium Browser Automation Project | Selenium")
        self.assertEqual(self.driver.current_url, "https://www.selenium.dev/documentation/")

        # self.driver.get("https://www.google.com")
        time.sleep(3)

    def test_2(self):
        """user able to scroll to the bottom of the page"""
        self.driver.get("https://www.selenium.dev/documentation/")
        self.driver.execute_script("window.scrollTo(0,2500);")
        # self.driver.get("https://www.wiki.com")
        time.sleep(3)

    def tearDown(self) -> None:
        # destroy driver instance
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

    # def test_2(self):
    #     # initialisation
    #     driver = webdriver.Edge()
    #     driver.set_window_size(1024, 768)
    #
    #     # test
    #     driver.get("https://www.wiki.com")
    #     self.assertTrue(False)
    #     # time.sleep(5)
    #
    #     # destroy driver instance
    #     driver.close()
#
# if __name__ == '__main__':
#     unittest.main()
    