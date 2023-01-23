import pandas as pd


# Read example data
df = pd.read_csv("../input/data.csv")


####################### METHOD 1 - USING where method #######################


df.where(df["name"] == "David")
