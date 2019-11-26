import allure
from pages.cheap_flight_pages.service_page import ServicePage
import config


def pytest_exception_interact(node, call, report):
    service_page = ServicePage()
    scrshot = service_page.get_screenshot()
    if config.browser != 'Safari':
        browser_log = service_page.get_browser_log()
    else:
        browser_log = ""
    allure.attach(
        body=scrshot,
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        body=browser_log,
        name='BrowserLog',
        attachment_type=allure.attachment_type.TEXT
    )
