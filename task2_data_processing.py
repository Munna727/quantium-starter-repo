import pandas as pd

files = [
    "daily_sales_data_0.csv",
    "daily_sales_data_1.csv",
    "daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(f"data/{file}")
    df = df[df["product"] == "pink morsel"]
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True)

df["price"] = (
    df["price"]
    .str.replace("$", "", regex=False)
    .astype(float)
)

df["sales"] = df["price"] * df["quantity"]

df = df[["sales", "date", "region"]]

df.to_csv("output.csv", index=False)

print(df)