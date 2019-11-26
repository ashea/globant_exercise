import random
import string
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webium import BasePage
from webium.driver import close_driver
import config
import pyperclip
import json
import ast


class ServicePage(BasePage):
    driver = BasePage._driver

    def randomword(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def get_browser_log(self):
        driver = self._driver
        file_name = 'BrowserLog_' + self.randomword(3) + '.txt'
        logfile = open(file_name, 'w')
        for entry in driver.get_log('browser'):
            if 'Warning' in str(entry) or 'Unexpected token' in str(entry):
                continue
            ast.literal_eval(json.dumps(entry))
            logfile.write(str(ast.literal_eval(json.dumps(entry['message']))) + '\n')
        logfile.close()
        logfile_text = open(file_name, 'r').read()
        pyperclip.copy(logfile_text)
        try:
            return pyperclip.paste()
        except UnicodeDecodeError:
            return 'Unable to provide log due to Unicode Error'

    def get_drivers(self):
        return self._driver

    def back_page(self):
        self._driver.back()

    def get_screenshot(self):
        screenshot = self._driver.get_screenshot_as_png()
        return screenshot

    def leave_only_one_tab(self):
        list_of_tabs = self._driver.window_handles
        while len(list_of_tabs) != 1:
            self._driver.switch_to.window(list_of_tabs[0])
            self._driver.close()
            list_of_tabs = self._driver.window_handles
            self._driver.switch_to.window(list_of_tabs[0])
        self._driver.switch_to.window(list_of_tabs[0])

    def close_driver_if_needed(self):
        if config.one_session:
            self.leave_only_one_tab()
        else:
            close_driver()

    def wait_until(self, time_set, element):
        WebDriverWait(self._driver, time_set).until(
            EC.presence_of_element_located((By.XPATH, element)))

    def wait_until_not(self, time_set, element):
        WebDriverWait(self._driver, time_set).until_not(
            EC.presence_of_element_located((By.XPATH, element)))
