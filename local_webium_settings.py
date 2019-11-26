from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Safari
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import config

if config.browser == 'Chrome':
    driver_class = Chrome
elif config.browser == 'Safari':
    driver_class = Safari
elif config.browser == 'Firefox':
    driver_class = Firefox
else:
    raise WebDriverException("No browser specified")
implicit_timeout = 5
wait_timeout = 50

default_search_type = By.XPATH
