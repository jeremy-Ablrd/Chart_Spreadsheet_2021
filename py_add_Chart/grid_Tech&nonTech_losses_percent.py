import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


years = []
for i in range(2010, 2022):
    years.append(i)

values = [10, 10, 11, 10, 11, 11, 8, 7, 7, 8, 5, 5]

# zip_list = list(zip(years, values))

print(years)
print(values)
# print(zip_list)
# {"Year": years, "Tech & Non-Tech losses": values}

df_final = pd.DataFrame([], index=years)
df_final["Tech & Non-Tech losses"] = values
print(df_final)

sns.set(style='white')

colors = ['#518D87']
df_final.plot(kind='line', stacked=False, color=colors, figsize=(12, 9))

# sns.lineplot(x="Year", y="Percentage %",
#              hue="", style="", palette='inferno',
#              data=df_final, markers=True, dashes=True)

plt.title('Technical and Non-technical Losses on Mahe and Praslin', fontsize=16)
plt.grid(visible=True, axis='y')

plt.xlabel('Year')
plt.xticks(rotation=0)
# plt.xlim(2009, 2022)
plt.ylabel("Percentage %")
# plt.ylim(2.9, 3.5)

plt.show()
