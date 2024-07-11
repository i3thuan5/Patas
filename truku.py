import pandas
import re
from os.path import basename

def xlsx轉錄音稿(xlsx檔名):
	語料名 = 找語料名(xlsx檔名)
	結果 = []
	for 篇名, dataframe in pandas.read_excel(
		xlsx檔名, engine='openpyxl',
		sheet_name=None,
	).items():
		結果.append(f"【{語料名}-{篇名}】")
		for tsua in dataframe.fillna('').itertuples():
			結果.append(f'{tsua.錄音編號}')
			結果.append(tsua.太魯閣語.strip())
			結果.append(tsua.華語.strip())
			結果.append('')
	return 結果[:-1]

def 找語料名(xlsx檔名):
	return re.search(r'D-[STP][LVTR]\d\d-\d\d\d', basename(xlsx檔名)).group(0)
