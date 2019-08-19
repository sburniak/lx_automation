from unittest import TestCase
from unittest.mock import Mock, MagicMock
from lx_auto import LxAccess


class TestRunBrowser(TestCase):

    def setUp(self):
        self.browser = LxAccess('random', "random")

    def test_preparation(self):
        pass