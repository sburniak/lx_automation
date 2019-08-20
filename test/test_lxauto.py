from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
import lx_auto


class TestRunBrowser(TestCase):

    def setUp(self):
        self.lx_a = lx_auto.LxAccess("fake_user", "fake_pass")
        # self.wb = webdriver
        # self.wb.Chrome = Mock()
        self.wb_chrome = patch("lx_auto.webdriver.Chrome")
        self.patcher = self.wb_chrome.start()

    def tearDown(self):
        self.patcher.stop()

    def test_preparation(self):
        self.lx_a.prepare_browser(self.patcher())
        self.patcher.assert_called_once()

    def test_go_to_page(self):
        self.lx_a.prepare_browser(self.patcher)
        self.lx_a.go_to_page(lx_auto.LX_LOGON)
        self.patcher.get.assert_called_with(lx_auto.LX_LOGON)

    def test_finish_browser(self):
        self.lx_a.prepare_browser(self.patcher)
        self.lx_a.finish_browser()
        self.patcher.quit.assert_called_once()

    def test_confirm_title_page(self):
        self.assertTrue(self.lx_a.confirm_title_page())

