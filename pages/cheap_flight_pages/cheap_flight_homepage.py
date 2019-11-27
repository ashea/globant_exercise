from selenium.webdriver.common.by import By
from webium import Find
from webium import BasePage
import config
import time
from selenium.webdriver.remote.errorhandler import ElementClickInterceptedException
import datetime
import pytz


class CheapFlightHomepage(BasePage):
    activeNextMonthArrow = Find(by=By.XPATH, value='.//div[contains(@id,"next") and not(@disabled)]')
    calendarWrapper = Find(by=By.XPATH, value='.//div[contains(@id,"displayWrapper")]')
    departureCity = Find(by=By.XPATH,
                         value='.//div[contains(@class,"gridCellOrigin")]/descendant::input[contains'
                               '(@placeholder,"Enter city or airport")]')
    departureDateField = Find(by=By.XPATH, value='.//div[contains(@id, "departDate-input")]')
    destinationCity = Find(by=By.XPATH,
                           value='.//div[contains(@class,"gridCellDestination")]/descendant::input[contains'
                                 '(@placeholder,"Enter city or airport")]')
    disabledNextDay = Find(by=By.XPATH,
                           value='((.//div[@class="month"]/descendant::div[contains(@class,"col-day") and not'
                                 '(contains(@class,"disabled")) and @data-val]/div[@class="day"])[last()]/following'
                                 '::div[contains(@class,"col-day disabled") and @data-val]/div[@class="day"])[1]')
    flightHotelTab = Find(by=By.XPATH, value='.//a[text()="Flight + Hotel"]')
    goToOriginalSite = Find(by=By.XPATH, value='.//a[text()="Go to Cheapflights.com instead"]')
    headerLogo = Find(by=By.XPATH, value='.//div[contains(@class,"logoContainer")]/descendant::span[@class="plane"]')
    lastAvailableDay = Find(by=By.XPATH,
                            value='(.//div[@class="month"]/descendant::div[contains(@class,"col-day") and not'
                                  '(contains(@class,"disabled")) and @data-val]/div[@class="day"])[last()]')
    logoContainer = Find(by=By.XPATH, value='.//div[contains(@class,"logoContainer")]')
    currentDay = Find(by=By.XPATH, value='.//div[@class="month"]/descendant::div[contains(@class,"col-day today")]')
    next10Days = Find(by=By.XPATH,
                      value='(.//div[@class="month"]/descendant::div[contains(@class,"col-day today")]/following::'
                            'div[@data-val]/div[@class="day"])[9]')
    next15Days = Find(by=By.XPATH,
                      value='(.//div[@class="month"]/descendant::div[contains(@class,"col-day today")]/following::'
                            'div[@data-val]/div[@class="day"])[14]')
    partnersPanel = Find(by=By.XPATH,
                         value='.//div[contains(@id,"slide")]/div[contains(text(),"Ha llegado el momento de '
                               'comparar")]')
    returnDateField = Find(by=By.XPATH, value='.//div[contains(@id, "returnDate-input")]')
    searchButton = Find(by=By.XPATH,
                        value='.//div[contains(@class,"gridCellSearchButton")]/button[contains(@class, "searchButton")'
                              ' and @type="submit"]')
    suggestedDestination = Find(by=By.XPATH,
                                value='(.//div[contains(@id,"smartbox-dropdown")]/descendant::ul[@role="listbox"]'
                                      '/li)[1]')
    viewButton = Find(by=By.XPATH, value='.//div[contains(@id,"slide")]/descendant::button[contains(text(),"Ver")][1]')

    url = config.url

    def __init__(self):
        super(CheapFlightHomepage, self).__init__()
        self.open()
        self._driver.maximize_window()

    def check_homepage_is_displayed(self):
        assert self.is_element_present("headerLogo", timeout=15), "Can't find headerLogo"
        assert self.is_element_present("goToOriginalSite", timeout=5), "Can't find goToOriginalSite"
        self.goToOriginalSite.click()
        self.validate_original_site_is_displayed()

    def move_to_next_tab(self):
        list_of_tabs = self._driver.window_handles
        self._driver.switch_to.window(list_of_tabs[1])

    def press_flight_hotel_tab(self):
        assert self.is_element_present("flightHotelTab", timeout=5), "Can't find flightHotelTab"
        self.flightHotelTab.click()

    def press_search_button(self):
        assert self.is_element_present("searchButton", timeout=5), "Can't find searchButton"
        try:
            self.searchButton.click()
        except ElementClickInterceptedException:
            assert self.is_element_present("next15Days", timeout=5), "Can't find next10Days"
            # Select 15th day from current date
            self.next15Days.click()
            time.sleep(0.5)
            self.searchButton.click()

    def press_view_from_partners_panel(self):
        assert self.is_element_present("viewButton", timeout=5), "Can't find viewButton"
        self.viewButton.click()

    def select_departure_date(self):
        assert self.is_element_present("departureDateField", timeout=15), "Can't find departureDateField"
        self.departureDateField.click()
        assert self.is_element_present("next10Days", timeout=10), "Can't find nextDays"
        # Select 10th day from current date
        self.next10Days.click()

    def select_destination_city(self, destination_city):
        assert self.is_element_present("destinationCity", timeout=5), "Can't find destinationCity"
        time.sleep(1)
        self.destinationCity.click()
        self.destinationCity.send_keys(' ')
        self.destinationCity.send_keys(destination_city)
        time.sleep(0.5)
        assert self.is_element_present("suggestedDestination", timeout=5), "Can't find suggestedDestination"
        self.suggestedDestination.click()
        time.sleep(1)

    def select_return_date(self):
        assert self.is_element_present("returnDateField", timeout=5), "Can't find returnDateField"
        self.returnDateField.click()
        assert self.is_element_present("next15Days", timeout=5), "Can't find next10Days"
        # Select 15th day from current date
        self.next15Days.click()

    def validate_departure_city_is_already_selected(self):
        assert self.is_element_present("departureCity", timeout=15), "Can't find departureCity"
        assert self.departureCity.get_attribute("value") == "Rosario (ROS)",\
            "Departure city is not selected or is wrong"

    def validate_I_can_pick_day_one_exact_year_from_today(self):
        assert self.is_element_present("departureDateField", timeout=15), "Can't find departureDateField"
        self.departureDateField.click()
        assert self.is_element_present("activeNextMonthArrow", timeout=5), "Can't find activeNextMonthArrow"
        active_arrow = True
        while active_arrow:
            self.activeNextMonthArrow.click()
            time.sleep(0.5)
            active_arrow = self.is_element_present("activeNextMonthArrow", timeout=3)
        assert self.is_element_present("lastAvailableDay", timeout=5), "Can't find lastAvailableDay"
        self.lastAvailableDay.click()

        # Get date one year from now
        my_date = datetime.datetime.now(pytz.timezone('Etc/GMT-3'))
        future_date = my_date.year + 1
        next_year_date = my_date.strftime("%m/%d/{}".format(str(future_date)))

        time.sleep(1)
        # Click here to close calendar view
        self.logoContainer.click()
        # Click again on Calendar
        time.sleep(0.5)
        self.departureDateField.click()
        # Get date selected value from calendar
        recover_date = self.departureDateField.text

        # Validate selected date is actually one year from current date
        assert str(next_year_date) == recover_date, "Selected date should be one year from now"

    def validate_next_day_is_disabled(self):
        # Locate right next day after current selected and verify is disabled by its locator
        assert self.is_element_present("disabledNextDay", timeout=5), "Can't find disabledNextDay"
        # Get day number
        day_number = int(self.disabledNextDay.text)
        assert day_number == int(self.lastAvailableDay.text) + 1, "Next day should be disabled"

    def validate_original_site_is_displayed(self):
        assert self.is_element_present("headerLogo", timeout=20), "Can't find headerLogo"
        assert "cheapflights.com" in self._driver.current_url, "URL is not right"

    def validate_partners_panel_is_displayed(self):
        assert self.is_element_present("partnersPanel", timeout=15), "Partners panel never showed up"
