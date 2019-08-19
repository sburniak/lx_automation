from selenium import webdriver


def get_driver():
    return webdriver.Chrome(r'C:\luxmed-automation\chromedriver.exe')

LX_LOGON = r"https://portalpacjenta.luxmed.pl/PatientPortal/Account/LogOn"


class LxAccess:

    def __init__(self, user, password):
        self._user = user
        self._password = password
        self._browser = None

    def prepare(self, browser):
        self._browser = browser
        self._browser.get(LX_LOGON)

    def finish_browser(self):
        self._browser.quit()

    def set_username(self):
        pass

    def confirm_title_page(self):
        return self._browser.title == "Portal Pacjenta LUX MED"


if __name__ == "__main__":
    lxA = LxAccess(1, 2)
    lxA.prepare(get_driver())
    print(lxA.confirm_title_page())
    lxA.finish_browser()
