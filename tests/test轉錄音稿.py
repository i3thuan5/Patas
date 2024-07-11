from unittest import TestCase
from os.path import join, dirname
from truku import xlsx轉錄音稿

class xlsx轉錄音稿試驗(TestCase):
    def test格式檢查(self):
        xlsx檔名 = join(
            dirname(__file__), '格式檢查', '1-4｜D-TL01-005.xlsx'
        )
        錄音稿檔名 = join(
            dirname(__file__), '格式檢查', '1-4｜D-TL01-005.txt'
        )
        結果 = xlsx轉錄音稿(xlsx檔名)
        with open(錄音稿檔名) as 檔案:
            self.assertEqual(結果, 檔案.read())
