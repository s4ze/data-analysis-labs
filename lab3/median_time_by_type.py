from data import *

shapes_type_count = pd.value_counts(df["shape"].values, sort=True)
shapes_type_count_keys, shapes_type_count_values = dict_sort(dict(shapes_type_count))
OBJECT_COUNT = len(shapes_type_count_keys)

shapes_durations_dict = {}
for i in shapes_type_count_keys:
    dfs = df[["duration (seconds)", "shape"]].loc[df["shape"] == i]
    shapes_durations_dict[i] = dfs["duration (seconds)"].median(axis=0) / 60.0 / 60.0

# shapes_durations_dict_keys, shapes_durations_dict_values = dict_sort(shapes_durations_dict)
shapes_durations_dict_keys = []
shapes_durations_dict_values = []
for k in shapes_type_count_keys:
    shapes_durations_dict_keys.append(k)
    shapes_durations_dict_values.append(shapes_durations_dict[k])

plt.title("Среднее время появление каждого объекта", fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(
    np.arange(OBJECT_COUNT), shapes_durations_dict_values, color=getColors(OBJECT_COUNT)
)
plt.xticks(
    np.arange(OBJECT_COUNT),
    shapes_durations_dict_keys,
    rotation=90,
    fontsize=PLOT_LABEL_FONT_SIZE,
)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel("Среднее время появления в часах", fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()
