from selenium.webdriver.common.by import By
from webium import Find
from webium import BasePage


class CheapFlightHomepage(BasePage):
    addANoteButton = Find(by=By.XPATH, value='.//body')
