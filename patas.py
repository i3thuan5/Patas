from argparse import ArgumentParser
import truku
import pangcah
import seediq


def main():
    parser = ArgumentParser(description='產生錄音稿')
    parser.add_argument('kari', choices=['Truku', 'Pangcah', 'Seediq'])
    parser.add_argument('xlsx檔名')
    args = parser.parse_args()
    if args.kari == 'Truku':
        xlsx轉錄音稿 = truku.xlsx轉錄音稿
    elif args.kari == 'Pangcah':
        xlsx轉錄音稿 = pangcah.xlsx轉錄音稿
    elif args.kari == 'Seediq':
        xlsx轉錄音稿 = seediq.xlsx轉錄音稿
    else:
        raise ValueError()
    with open(args.xlsx檔名 + '.txt', 'wt') as 檔案:
        for 行 in xlsx轉錄音稿(args.xlsx檔名):
            print(行, file=檔案)


if __name__ == '__main__':
    main()
