# Patas

Google Sheet轉錄音稿程式

## 設定環境

開「終端機」，輸入：

```bash
git clone https://github.com/i3thuan5/Patas.git
cd Patas
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 轉錄音稿

從Google Sheet下載錄音稿，假設下載後檔名是`1-465｜D-TL01-005.xlsx`

```bash
cd Patas
source venv/bin/activate
python patas.py Truku ~/Downloads/1-465｜D-TL01-005.xlsx
```

執行完會產生`1-465｜D-TL01-005.xlsx.txt`檔案。

### Nitilidan no Pangcah

從Google Sheet下載錄音稿，假設下載後檔名是`D-PV01｜1~534 (C-PL002).xlsx`

```bash
cd Patas
source venv/bin/activate
python patas.py Pangcah ~/Downloads/D-PV01｜1\~534\ \(C-PL002\).xlsx
```

執行完會產生`D-PV01｜1~534 (C-PL002).xlsx.txt`檔案。
