import pandas as pd
import matplotlib.pyplot as plt
sales_data = pd.read_csv("company_sales_data.csv")
plt.figure(figsize=(11, 6))
plt.plot(sales_data["month_number"], sales_data["total_profit"],
         color="red",
         linestyle="--",
         marker="o",
         linewidth=3,
         markerfacecolor="red",
         markersize=8,
         label="profit data of last year")
plt.title("company sales data of last year")
plt.xlabel("month number")
plt.ylabel("sold units number")
plt.xticks(sales_data["month_number"])
plt.ylim(100000, 500000)
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()
           
