from data import *

MONTH_COUNT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MONTH_NAMES = [
    "Янв",
    "Фев",
    "Мар",
    "Апр",
    "Май",
    "Июн",
    "Июл",
    "Авг",
    "Сен",
    "Окт",
    "Ноя",
    "Дек",
]


def convert_datetime(dt_str):
    try:
        return pd.to_datetime(dt_str, format="%m/%d/%Y %H:%M")
    except ValueError:
        if "24:00" in dt_str:
            date_part, _ = dt_str.split(" ")
            dt = pd.to_datetime(date_part, format="%m/%d/%Y") + pd.Timedelta(days=1)
            return dt.replace(hour=0, minute=0)
        return pd.NaT


df["datetime_parsed"] = df["datetime"].apply(convert_datetime)
df["month"] = df["datetime_parsed"].dt.month
monthly_median = (
    df.groupby("month")["duration (seconds)"].mean().div(3600).reset_index()
)

plt.figure(figsize=(12, 6))
plt.bar(
    monthly_median["month"], monthly_median["duration (seconds)"], color=getColors(12)
)
plt.xticks(range(1, 13), MONTH_NAMES, rotation=45, ha="right")
plt.ylabel("Медианное время (часы)")
plt.title("Длительность наблюдений по месяцам")
plt.tight_layout()
plt.show()
