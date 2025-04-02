from data import *

shapes_type_count = pd.value_counts(df["shape"].values, sort=True)
shapes_type_count_keys, shapes_type_count_values = dict_sort(dict(shapes_type_count))
OBJECT_COUNT = len(shapes_type_count_keys)
plt.title("Типы объектов", fontsize=PLOT_LABEL_FONT_SIZE)
bar = plt.bar(
    np.arange(OBJECT_COUNT), shapes_type_count_values, color=getColors(OBJECT_COUNT)
)
plt.xticks(
    np.arange(OBJECT_COUNT),
    shapes_type_count_keys,
    rotation=90,
    fontsize=PLOT_LABEL_FONT_SIZE,
)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel("Сколько раз видели", fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()
