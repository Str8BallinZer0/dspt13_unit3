import pandas as pd
import time

df = pd.DataFrame([[3, 7, 5, ], [3, 6, 1], [4, 7, 6]])


def add_1(dataframe):
    for x in range(10):
        time.sleep(2)
        dataframe = dataframe + 1
        print(dataframe)