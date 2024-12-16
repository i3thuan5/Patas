import pandas
import re
from os.path import basename
from argparse import ArgumentParser
from pangcah import 找語料名


def xlsx轉錄音稿(xlsx檔名):
    語料名 = 找語料名(xlsx檔名)
    結果 = []
    錄音編號 = None
    for 篇名, dataframe in pandas.read_excel(
        xlsx檔名, engine='openpyxl',
        sheet_name=None,
    ).items():
        結果.append(f"【{語料名}-{篇名}】")
        print("篇名", 篇名)
        for 行 in dataframe.fillna('').itertuples():
            if 錄音編號 is not None and 行.錄音編號 != 錄音編號 + 1:
                raise ValueError(f"「{篇名}」裡的錄音編號{行.錄音編號}應該要是{錄音編號+1}")
            結果.append(f'{行.錄音編號}')
            結果.append(getattr(行, 'Seediq Tgdaya 語').strip())
            結果.append('')
            錄音編號 = 行.錄音編號
    return 結果[:-1]


def main():
    parser = ArgumentParser(description='產生錄音稿')
    parser.add_argument('xlsx檔名')
    args = parser.parse_args()
    with open(args.xlsx檔名 + '.txt', 'wt') as 檔案:
        for 行 in xlsx轉錄音稿(args.xlsx檔名):
            print(行, file=檔案)


if __name__ == '__main__':
    main()
