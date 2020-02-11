from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/ps-trakotor/Testfile/chromedriver')
driver.get('https://www.airbnb.co.uk/c/danw6')

title = driver.title
print(title)

assert title =='Get £34 off your first adventure!'