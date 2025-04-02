from data import *

MONTH_COUNT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MONTH_LABEL = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
]

for i in df["datetime"]:
    m, d, y_t = i.split("/")
    MONTH_COUNT[int(m) - 1] = MONTH_COUNT[int(m) - 1] + 1

plt.bar(np.arange(12), MONTH_COUNT, color=getColors(12))
plt.xticks(np.arange(12), MONTH_LABEL, rotation=90, fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel("Частота появления", fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.title("Частота появления объектов по месяцам", fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()
