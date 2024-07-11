import pandas

def xlsx轉錄音稿(xlsx檔名):
	結果 = []
	for 篇名, dataframe in pandas.read_excel(
		xlsx檔名, engine='openpyxl',
		sheet_name=None
	).items():
		print(篇名, dataframe)
		結果.append(f"【{篇名}】")
		for tsua in dataframe.fillna('').itertuples():
			print('tsua', tsua)
			結果.append(f'{tsua.錄音編號}')
			結果.append(tsua.太魯閣語)
			結果.append(tsua.華語)
			結果.append('')

	return 結果
