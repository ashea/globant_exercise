from pages.cheap_flight_pages.service_page import ServicePage


class BaseTest(object):
    service_page = ServicePage()

    @classmethod
    def teardown_class(self):
        self.service_page.close_driver_if_needed()
