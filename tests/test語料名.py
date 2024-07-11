from unittest import TestCase
from os.path import join, abspath, dirname
from truku import 找語料名


class 語料名試驗(TestCase):
    def test格式檢查(self):
        xlsx檔名 = join(
            abspath(dirname(__file__)), '格式檢查', '1-4｜D-TL01-005.xlsx'
        )
        self.assertEqual(找語料名(xlsx檔名), 'D-TL01-005', xlsx檔名)
