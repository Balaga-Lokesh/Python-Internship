import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
grouped = df.groupby("product")["amount"].sum()
grouped.plot(kind="bar")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Sales by Product")
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()
