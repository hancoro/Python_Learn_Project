# Selenium PIP was installed
# Location is LIB\site-packages\selenium

from selenium import webdriver
url = "http://www.avakin.com/"
results_folder = "C:\\Users\\hancoro\\PycharmProjects\\StuckInBebProject\\SeleniumResults\\"
chrome_driver_location = "C:\\RPH_Drivers\\chromedriver.exe"

# This creates the webdriver
driver = webdriver.Chrome(chrome_driver_location)

# This navigates to the the url specified
driver.get(url)
driver.set_page_load_timeout(10)


def selenium_wrapper(xpath, action, sendkeytext):
    try:
        if action == "click":
            driver.find_element_by_xpath(xpath).click()
        elif action == "type":
            driver.find_element_by_xpath(xpath).send_keys(sendkeytext)
        elif action == "clear":
            driver.find_element_by_xpath(xpath).clear()
        else:
            print("Selected action: '" + action + " is not included in the selenium wrapper")
    except ZeroDivisionError as err:
        print(err)
    return ""


#
selenium_wrapper("//button[@id='catapultCookie']", "click", "")
driver.maximize_window()
driver.get_screenshot_as_file(results_folder + "Avakin_Landing_Page.png")
selenium_wrapper("//li[@id='menu-item-67']/a", "click", "")
driver.get_screenshot_as_file(results_folder + "Avakin_WhatsNew_Page.png")
driver.close()
driver.quit()







