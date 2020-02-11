import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    def test_demo_login(self):
        driver = webdriver.Chrome(executable_path='/home/ps-trakotor/Testfile/chromedriver')
        driver.get('https://www.reserved.com/pl/pl/')
        title = driver.title
        print(title)
        assert 'Reserved & Shop Online' == title
        driver.quit()

    def test_demo_account(self):
        driver = webdriver.Chrome(executable_path='/home/ps-trakotor/Testfile/chromedriver')
        driver.get('https://www.reserved.com/pl/pl/woman')
        title = driver.title
        print(title)
        assert 'Moda damska | RESERVED' == title
        driver.quit()