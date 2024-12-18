from argparse import ArgumentParser
from pathlib import Path
from truku import xlsx轉錄音稿kari


def main():
    parser = ArgumentParser(description='產生錄音稿')
    parser.add_argument('kari', choices=['Truku', 'Pangcah', 'Seediq'])
    parser.add_argument('xlsx檔名', type=Path)
    args = parser.parse_args()
    if args.kari == 'Truku':
        kari = '太魯閣語'
    elif args.kari == 'Pangcah':
        kari = '阿美語'
    elif args.kari == 'Seediq':
        kari = 'Tgdaya'
    else:
        raise ValueError()

    txt檔名 = args.xlsx檔名.parent / (args.xlsx檔名.stem + '.txt')
    with open(txt檔名, 'wt') as 檔案:
        for 行 in xlsx轉錄音稿kari(args.xlsx檔名, kari):
            print(行, file=檔案)

    if args.kari == 'Truku':
        csv檔名 = args.xlsx檔名.parent / (args.xlsx檔名.stem + '.csv')
        truku.xlsx轉csv(args.xlsx檔名, csv檔名)


if __name__ == '__main__':
    main()
