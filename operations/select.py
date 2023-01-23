import pandas as pd


# Read example data
df = pd.read_csv("../input/data.csv")


####################### METHOD 1 - USING [] #######################


df["name"]  # Select one column
# Output:
#   name
# 0 David
# 1 Lily
# 2 Ryan


df[["name", "age"]]  # Select two+ column
# Output:
# 	name	age
# 0	David	25
# 1	Lily	29
# 2	Ryan	60

####################### METHOD 2 - loc #######################

df.loc[:, ["name", "age", "weight"]]  # Select one+ columns
# Output:
# 	name	age	weight
# 0	David	25	80
# 1	Lily	29	60
# 2	Ryan	60	100

####################### METHOD 3 - . #######################

df.name  # Select only one column
# Output:
#   name
# 0 David
# 1 Lily
# 2 Ryan
