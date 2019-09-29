import pandas as pd


df = pd.read_csv('CDD.csv', delimiter="\t")

print()
print(df["EVENT CATEGORY"].unique())
print()
print(df.info())
print()
print()
print(df["ESTIMATED TOTAL COST"].describe())
