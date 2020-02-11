from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/ps-trakotor/Testfile/chromedriver')
# driver.get('https://www.quiksilver.com/original-collection/#?intcmp=qs_425419')
driver.get('https://www.reserved.com/pl/pl/')

title = driver.title
print(title)
assert title == 'Reserved & Shop Online'