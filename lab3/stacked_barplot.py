from data import *

top_cities = df["city"].value_counts().nlargest(10).index
filtered_df = df[df["city"].isin(top_cities)]

city_shape_counts = filtered_df.groupby(["city", "shape"]).size().unstack().fillna(0)

city_shape_counts = city_shape_counts.loc[
    city_shape_counts.sum(axis=1).sort_values(ascending=False).index
]

plt.figure(figsize=(8, 7))
colors = getColors(len(city_shape_counts.columns))

bottom = None
for i, shape in enumerate(city_shape_counts.columns):
    plt.bar(
        city_shape_counts.index,
        city_shape_counts[shape],
        bottom=bottom,
        label=shape,
        color=colors[i],
    )
    bottom = (
        city_shape_counts[shape]
        if bottom is None
        else bottom + city_shape_counts[shape]
    )

plt.title("Распределение форм НЛО по городам (топ-10)", fontsize=16)
plt.xlabel("Город", fontsize=14)
plt.ylabel("Количество наблюдений", fontsize=14)
plt.xticks(rotation=45, ha="right")
plt.legend(title="Форма НЛО", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()
