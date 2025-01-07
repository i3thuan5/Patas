from unittest import TestCase
from os.path import join, abspath, dirname
from csv import DictReader
from kari import xlsx轉csv


class xlsx轉csv試驗(TestCase):
    def test格式檢查(self):
        self.maxDiff = None
        xlsx檔名 = join(
            abspath(dirname(__file__)), '格式檢查', '1-4｜D-TL01-005.xlsx'
        )
        csv檔名 = join(
            abspath(dirname(__file__)), '格式檢查', '1-4｜D-TL01-005.csv'
        )
        xlsx轉csv(xlsx檔名, '太魯閣語', csv檔名)
        答案 = {
            '音檔檔名': 'E-TV001-0004.wav',
            '錄音編號': '4',
            '篇名': '我眺望山嶺時',
            '太魯閣語': (
                'Paah ku laqi bilaq bitaq sayang, '
                'yaa hmuya ma ku smkuxul bi mquri dgiyaq qmita! '
                'Manu bi pusu na msa ku lmnglung?'
            ),
            '華語': '從小至今，不知為何總是喜歡跳望山嶺！到底是何因由呢？',
        }
        with open(csv檔名) as 檔案:
            self.assertEqual(答案, list(DictReader(檔案))[3])
