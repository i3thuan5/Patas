import pandas
import re
from os.path import basename
from csv import DictWriter


def xlsx轉錄音稿(xlsx檔名):
    語料名 = 找語料名(xlsx檔名)
    結果 = []
    錄音編號 = None
    for 篇名, dataframe in 讀xlsx資料(xlsx檔名):
        結果.append(f"【{語料名}-{篇名}】")
        for 行 in dataframe:
            if 錄音編號 is not None and 行.錄音編號 != 錄音編號 + 1:
                raise ValueError(f"「{篇名}」裡的錄音編號{行.錄音編號}應該要是{錄音編號+1}")
            結果.append(f'{行.錄音編號}')
            結果.append(行.太魯閣語.strip())
            結果.append('')
            錄音編號 = 行.錄音編號
    return 結果[:-1]


def xlsx轉csv(xlsx檔名, csv檔名):
    with open(csv檔名, 'wt') as 檔案:
        writer = DictWriter(檔案, fieldnames=[
            '錄音編號', '篇名', '太魯閣語', '華語',
        ])
        writer.writeheader()
        for 篇名, dataframe in 讀xlsx資料(xlsx檔名):
            for 行 in dataframe:
                writer.writerow({
                    '錄音編號': 行.錄音編號,
                    '篇名': 篇名.strip(),
                    '太魯閣語': 行.太魯閣語.strip(),
                    '華語': 行.華語.strip(),
                })


def 找語料名(xlsx檔名):
    return re.search(r'D-[STP][LVTR]\d\d-\d\d\d', basename(xlsx檔名)).group(0)


def 讀xlsx資料(xlsx檔名):
    for 篇名, dataframe in pandas.read_excel(
        xlsx檔名, engine='openpyxl',
        sheet_name=None,
    ).items():
        yield 篇名, dataframe.fillna('').itertuples()
