from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import chromedriver_binary


try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/')

    driver.close();
    driver.quit();

except Exception as e:
    print (e)
