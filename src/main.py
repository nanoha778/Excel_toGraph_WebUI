from matplotlib import figure
import pandas as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt

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



    output_df = date_sorted_df

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    fig = fig.set_size_inches((12, 7))
    

    sns.set_theme(style="whitegrid")

    plt.tight_layout()
    plt.subplots_adjust(
    left=0.1,
    right=0.9,
    top=0.95,
    bottom=0.12
    )
    
    plt.xticks(rotation=45, ha="right")

    sns.barplot(data=output_df, x="date", y="amount", ax=ax1)

    sns.lineplot(data=output_df, x="date", y="sales", ax=ax2, marker="o")

    plt.legend(loc="upper left", frameon=False)

    plt.show()

    plt.savefig("graph.png")
    plt.close()

    output_df = output_df.rename(columns=lambda c: COLUMN_OUTPUT.get(c, c))

    print(output_df.head())


# run
if __name__ == "__main__":
    main()