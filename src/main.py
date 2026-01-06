from matplotlib import rcParams
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

def logger(log : str):
    print(log)

def input():
    try:
        path=''
        if "--input" in sys.argv:
            path = sys.argv[sys.argv.index("--input") + 1]
    except:
        logger("読み込み先ファイルパスが存在しません")
        sys.exit()
    return path

def output():
    try:
        path='graph.png'
        if "--output" in sys.argv:
            path = sys.argv[sys.argv.index("--output") + 1]
    except:
        logger("保存先ファイルパスが存在しません")
        sys.exit()
    return path


def debug_mode():
    isDebug = False
    if "--debug" in sys.argv:
        isDebug = True
    return isDebug

def dataframe_sort(path : str ='./sample/data.xlsx'):
    try:
        df = pd.DataFrame(pd.read_excel(path))
    except:
        logger("ファイルが存在しません")
        sys.exit()

    df = df.rename(columns=lambda c: COLUMN_ALIAS.get(c, c))

    date_sorted_df = df.groupby("date", as_index=False)[["sales", "amount"]].sum()
    if (debug_mode()):
        logger(date_sorted_df)
    return date_sorted_df


def make_image(df=[[]], output_path='graph.png', title="売上高"):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    fig = fig.set_size_inches((12, 7))
    

    sns.set_theme(style="whitegrid")

    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

    plt.tight_layout()
    plt.subplots_adjust(
    left=0.07,
    right=0.93,
    top=0.9,
    bottom=0.1
    )
    
    plt.xticks(rotation=45, ha="right")

    try:
        ax1.set_ylabel("件数")
        ax2.set_ylabel("売上")

        ax1.set_xlabel("日付け")
    except:
        logger("フォントが存在しません")

    sns.barplot(data=df, x="date", y="amount", ax=ax1)

    sns.lineplot(data=df, x="date", y="sales", ax=ax2, marker="o")

    plt.title(title)
    plt.savefig(output_path)


    if (debug_mode()):
        plt.show()

    plt.close()

    df = df.rename(columns=lambda c: COLUMN_OUTPUT.get(c, c))


# test
def debug():
    df = dataframe_sort(input())
    make_image(df, output())

def main():
    print("未実装")
    

    


# run
if __name__ == "__main__":
    debug()