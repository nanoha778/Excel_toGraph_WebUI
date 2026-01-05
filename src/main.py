import pandas as pd
import sys

# test
def main():

    path='./data.xlsx'

    if "--input" in sys.argv:
        path = sys.argv[sys.argv.index("--input") + 1]

    df = pd.DataFrame(pd.read_excel(path))
    
    print(df.head())



# run
if __name__ == "__main__":
    main()