import pandas as pd
import sys


COLUMN_ALIAS = {
    "日付" : "date",
    "日付け" : "date",
    "date" : "date",
    "売上" : "sales",
    "売り上げ" : "sales",
    "売上げ" : "sales",
    "sales" : "sales",
    "件数" : "amount",
    "amount" : "amount",
    "カテゴリ" : "category",
    "category" : "category"
}

COLUMN_OUTPUT = {
    "date" : "日付け",
    "sales" : "売上",
    "amount" : "件数",
    "category" : "カテゴリ"
}

# test
def main():

    path='./sample/data.xlsx'

    if "--input" in sys.argv:
        path = sys.argv[sys.argv.index("--input") + 1]

    df = pd.DataFrame(pd.read_excel(path))

    df = df.rename(columns=lambda c: COLUMN_ALIAS.get(c, c))

    date_sorted_df = df.groupby("date", as_index=False)[["sales", "amount"]].sum()

    print(date_sorted_df.head())



# run
if __name__ == "__main__":
    main()