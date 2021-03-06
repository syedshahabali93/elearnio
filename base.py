import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def launch_browser():
    print("Launching browser")
    global driver, wait1, wait2, wait3
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=1")
    options.add_argument("--start-maximized")
    # options.add_argument("user-agent="+chromeUserAgent)
    options.add_argument("--window-size=1980x1080")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--single-process')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.binary_location = "/tmp/bin/headless-chromium"
    chromedriver_path = "/tmp/bin/chromedriver"

    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'browser': 'ALL'}
    d['goog:loggingPrefs'] = {'performance': 'ALL'}

    driver = webdriver.Chrome(options=options, executable_path=chromedriver_path, desired_capabilities=d,
                              service_args=["--verbose", "--log-path=/tmp/results/chrome1.log"],
                              service_log_path="/tmp/results/chrome2.log")
    wait1 = WebDriverWait(driver, 10)
    wait2 = WebDriverWait(driver, 30)
    wait3 = WebDriverWait(driver, 90)
    driver.maximize_window()
    print(driver.execute_script("return navigator.userAgent;"))


def clear_text(ele):
    driver.find_element(*ele).clear()


def enter_text(ele, text):
    driver.find_element(*ele).send_keys(text)


def click(ele):
    driver.find_element(*ele).click()


def wait_and_clear_text(ele):
    wait2.until(EC.visibility_of_element_located((ele))).clear()


def wait_for_element_visible(ele):
    wait2.until(EC.visibility_of_element_located((ele)))


def find_element(ele):
    return driver.find_element(*ele)


def find_all_elements(ele):
    return driver.find_elements(*ele)


def wait3_and_find_element(ele):
    return wait3.until(EC.visibility_of_element_located((ele)))


def wait1_and_find_element(ele):
    return wait1.until(EC.visibility_of_element_located((ele)))


def wait_and_find_all_elements(ele):
    return wait2.until(EC.visibility_of_all_elements_located((ele)))


def wait3_and_find_all_elements(ele):
    return wait3.until(EC.visibility_of_all_elements_located((ele)))


def wait1_and_find_all_elements(ele):
    return wait1.until(EC.visibility_of_all_elements_located((ele)))


def scroll_to_element(ele):
    print("inside scroll")
    driver.execute_script("arguments[0].scrollIntoView();", ele)
    time.sleep(1)


def move_to_element(ele):
    action = ActionChains(driver)
    action.move_to_element(ele).perform()


def enter_text_in_element(ele, text):
    ele.send_keys(text)


def get_current_url():
    return driver.current_url


def close_browser():
    if (browser_already_open()):
        driver.quit()


def get_xpath(tuple, name):
    return (tuple[0], tuple[1].replace("to_be_replaced", name))


def get_console_logs():
    pass
    # print("#####"*10 + " CONSOLE LOGS " + "#####"*10)
    # for entry in driver.get_log('browser'):
    #     print(entry)

    # print("#####"*10 + " NETWORK LOGS " + "#####"*10)
    # for entry in driver.get_log('performance'):
    #     print(entry)


def load_url(base_url):
    print("Loading url")
    driver.get(base_url)


def wait_and_enter_text(ele, text):
    print("Entering Email or password")
    print(text)
    wait1.until(EC.visibility_of_element_located((ele))).send_keys(text)


def wait_and_click(element_name, ele):
    print("Clicking on: " + element_name)
    wait1.until(EC.visibility_of_element_located((ele))).click()


def wait_and_find_element(ele):
    return wait1.until(EC.visibility_of_element_located((ele)))


def wait_for_element_invisible(ele):
    wait1.until(EC.invisibility_of_element_located((ele)))


def drag_and_drop(element, x, y):
    ActionChains(driver).drag_and_drop_by_offset(element, x, y).perform()


def is_element_present(ele):
    count = len(driver.find_elements(*ele))
    if (count == 0):
        return False
    else:
        return True


def capture_screenshot(filename):
    driver.get_screenshot_as_file(filename)


def close_browser():
    if (browser_already_open()):
        driver.quit()


def browser_already_open():
    try:
        global driver
        if (len(driver.window_handles) == 1):
            return True
        else:
            return False
    except Exception as e:
        return False

