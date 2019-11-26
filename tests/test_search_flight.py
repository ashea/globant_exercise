"""
Test to validate Cheap Flight page
"""
import pytest
from tests.base_test import BaseTest
from pages.cheap_flight_pages.cheap_flight_homepage import CheapFlightHomepage
import config


class TestSearchFlight(BaseTest):
    cf_homepage = CheapFlightHomepage()

    @pytest.mark.skipif(config.quick_test, reason="skipped as a quick test is activated")
    def test_search_flight(self):
        pass
