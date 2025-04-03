from data import *

data = df.groupby("shape")["duration (seconds)"].median().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
data.plot(kind="bar", color=getColors(len(data)))

plt.ylabel("Форма НЛО", fontsize=12)
plt.xlabel("Медианная длительность (секунды)", fontsize=12)
plt.title("Длительность наблюдения по формам НЛО", fontsize=14)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
