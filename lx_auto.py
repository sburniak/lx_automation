import time

from selenium import webdriver
from selenium.webdriver import ActionChains


def get_driver():
    return webdriver.Chrome(r'C:\luxmed-automation\chromedriver.exe')

LX_LOGON = r"https://portalpacjenta.luxmed.pl/PatientPortal/Account/LogOn"
LX_LOGON1 = r"file:///C:/Users/Seba/Desktop/panelLogowania/Portal%20Pacjenta%20LUX%20MED.html"


class LxAccess:
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self.browser = None

    def prepare_browser(self, browser):
        self.browser = browser

    def go_to_page(self, page):
        self.browser.get(page)

    def finish_browser(self):
        self.browser.quit()

    def set_username(self):
        login = self.browser.find_element_by_id("Login")
        login.send_keys(self._user)

    def set_password(self):
        pswd = self.browser.find_element_by_xpath("//input[@id='Password']")
        pswd.send_keys(self._password)

    def confirm_title_page(self):
        return self.browser.title == "Portal Pacjenta LUX MED"

    def execute_script(self):
        self.browser.execute_script('document.getElementById("Password").removeAttribute("style")')

    def click_submit(self):
        bttn = self.browser.find_element_by_xpath("//input[@type='submit']")
        bttn.click()


if __name__ == "__main__":
    lxA = LxAccess('1', '2')
    lxA.prepare_browser(get_driver())
    lxA.go_to_page(LX_LOGON1)
    print(lxA.confirm_title_page())
    lxA.execute_script()
    lxA.set_username()
    lxA.set_password()
    lxA.click_submit()
    lxA.go_to_page("https://portalpacjenta.luxmed.pl/PatientPortal/Reservations/Coordination")
    # lxA.finish_browser()
