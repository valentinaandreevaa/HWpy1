from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")

    for  _ in range(3):
        blue_button = driver.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        sleep(2)

        driver.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    driver.quit()


driver = webdriver.Firefox()

try:
    driver.get("http://uitestingplayground.com/classattr")

    for  _ in range(3):
        blue_button = driver.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        sleep(2)
        
        driver.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    driver.quit()