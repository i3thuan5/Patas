from argparse import ArgumentParser
from pathlib import Path
import truku
import pangcah
import seediq


def main():
    parser = ArgumentParser(description='產生錄音稿')
    parser.add_argument('kari', choices=['Truku', 'Pangcah', 'Seediq'])
    parser.add_argument('xlsx檔名', type=Path)
    args = parser.parse_args()
    if args.kari == 'Truku':
        xlsx轉錄音稿 = truku.xlsx轉錄音稿
    elif args.kari == 'Pangcah':
        xlsx轉錄音稿 = pangcah.xlsx轉錄音稿
    elif args.kari == 'Seediq':
        xlsx轉錄音稿 = seediq.xlsx轉錄音稿
    else:
        raise ValueError()

    txt檔名 = args.xlsx檔名.parent / (args.xlsx檔名.stem + '.txt')
    with open(txt檔名, 'wt') as 檔案:
        for 行 in xlsx轉錄音稿(args.xlsx檔名):
            print(行, file=檔案)

    if args.kari == 'Truku':
        csv檔名 = args.xlsx檔名.parent / (args.xlsx檔名.stem + '.csv')
        truku.xlsx轉csv(args.xlsx檔名, csv檔名)


if __name__ == '__main__':
    main()
