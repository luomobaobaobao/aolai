from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_center_page import PersonCenterPage
from page.setting_page import SettingPage
from page.sign_in_page import SingInPage



class NavigationPage:

    def __init__(self,driver):
        self.driver = driver

    def get_home_page(self):
        return HomePage(self.driver)

    def get_login_page(self):
        return LoginPage(self.driver)

    def get_person_center_page(self):
        return PersonCenterPage(self.driver)

    def get_setting_page(self):
        return SettingPage(self.driver)

    def get_sign_in_page(self):
        return SingInPage(self.driver)

