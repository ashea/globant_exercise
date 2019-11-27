from selenium.webdriver.common.by import By
from webium import Find
from webium import BasePage


class FlightResultsPage(BasePage):
    flightList = Find(by=By.XPATH, value='.//div[@id="flight-listings"]')
    flightPrice = Find(by=By.XPATH,
                       value='(.//article[contains(@class,"contract-block")]/descendant::strong[contains(@id,'
                             '"TOTALFARE")]/span)[1]')

    def validate_flight_results_page_is_displayed(self):
        self.is_element_present("flightList", timeout=30), "flightList was not displayed"
        assert "air/Listing/" in self._driver.current_url, "Flights list url is not right"

    def validate_price_from_first_result_is_more_than_zero(self):
        self.is_element_present("flightPrice", timeout=10), "Can't find flightPrice"
        # Get price value from first result
        price = self.flightPrice.get_attribute('defaultvalue')
        assert price > 0, "Price value should be positive"
