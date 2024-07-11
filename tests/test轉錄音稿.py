from unittest import TestCase
from os.path import join, abspath, dirname
from truku import xlsx轉錄音稿

class xlsx轉錄音稿試驗(TestCase):
    def test格式檢查(self):
        self.maxDiff = None
        xlsx檔名 = join(
            abspath(dirname(__file__)), 'patas格式檢查', '1-4｜D-TL01-005.xlsx'
        )
        錄音稿檔名 = join(
            abspath(dirname(__file__)), 'patas格式檢查', '1-4｜D-TL01-005.txt'
        )
        結果 = xlsx轉錄音稿(xlsx檔名)
        答案 = []
        with open(錄音稿檔名) as 檔案:
            for 行 in 檔案.readlines():
                答案.append(行.rstrip())
        self.assertEqual(結果, 答案)
