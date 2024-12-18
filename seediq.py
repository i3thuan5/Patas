import pandas
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
            結果.append(getattr(行, 'Tgdaya').strip())
            結果.append('')
            錄音編號 = 行.錄音編號
    return 結果[:-1]
