"""
Test to validate Cheap Flight page
"""
import pytest
from tests.base_test import BaseTest
from pages.cheap_flight_pages.cheap_flight_homepage import CheapFlightHomepage
from pages.cheap_flight_pages.flight_results_page import FlightResultsPage
import config


class TestSearchFlight(BaseTest):
    cf_homepage = CheapFlightHomepage()
    flight_results_page = FlightResultsPage()

    def test_search_flight(self):
        self.cf_homepage.check_homepage_is_displayed()
        self.cf_homepage.press_flight_hotel_tab()
        self.cf_homepage.validate_departure_city_is_already_selected()
        self.cf_homepage.select_destination_city("Bogota, Colombia - El Dorado")
        self.cf_homepage.select_departure_date()
        self.cf_homepage.select_return_date()
        self.cf_homepage.press_search_button()
        self.cf_homepage.validate_partners_panel_is_displayed()
        self.cf_homepage.press_view_from_partners_panel()
        self.cf_homepage.move_to_next_tab()
        self.flight_results_page.validate_flight_results_page_is_displayed()
        self.flight_results_page.validate_price_from_first_result_is_more_than_zero()
