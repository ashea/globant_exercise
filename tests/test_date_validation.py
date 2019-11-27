"""
Test to validate date calendar
"""
from tests.base_test import BaseTest
from pages.cheap_flight_pages.cheap_flight_homepage import CheapFlightHomepage
import pytest
import config


class TestDateValidation(BaseTest):
    cf_homepage = CheapFlightHomepage()

    @pytest.mark.skipif(config.quick_test, reason="skipped as a quick test is activated")
    def test_date_validation(self):
        self.cf_homepage.check_homepage_is_displayed()
        self.cf_homepage.press_flight_hotel_tab()
        self.cf_homepage.validate_I_can_pick_day_one_exact_year_from_today()
        self.cf_homepage.validate_next_day_is_disabled()
