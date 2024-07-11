# Patas

Google Sheet轉錄音稿程式

## 設定環境

開「終端機」，輸入：

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 轉錄音稿

從Google Sheet下載錄音稿，假設下載後檔名是`1-465｜D-TL01-005.xlsx`

```bash
source venv/bin/activate
python truku.py ~/Downloads/1-465｜D-TL01-005.xlsx
```

執行完會產生`1-465｜D-TL01-005.xlsx.txt`檔案。
