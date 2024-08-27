from unittest import TestCase
from os.path import join, abspath, dirname
from pangcah import 找語料名
from pangcah import xlsx轉錄音稿


class 語料名試驗(TestCase):
    def test格式檢查(self):
        xlsx檔名 = join(
            abspath(dirname(__file__)),
            '格式檢查', 'D-PV01｜1~353 (C-PL002)sample.xlsx'
        )
        self.assertEqual(找語料名(xlsx檔名), 'D-PV01', xlsx檔名)


class xlsx轉錄音稿試驗(TestCase):
    def test格式檢查(self):
        self.maxDiff = None
        xlsx檔名 = join(
            abspath(dirname(__file__)),
            '格式檢查', 'D-PV01｜1~353 (C-PL002)sample.xlsx'
        )
        錄音稿檔名 = join(
            abspath(dirname(__file__)),
            '格式檢查', 'D-PV01｜1~353 (C-PL002)sample.txt'
        )
        結果 = xlsx轉錄音稿(xlsx檔名)
        答案 = []
        with open(錄音稿檔名) as 檔案:
            for 行 in 檔案.readlines():
                答案.append(行.rstrip())
        self.assertEqual(結果, 答案)
