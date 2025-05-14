import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_percentile_ci(bootstrap_stats, pe, alpha):
    left, right = np.quantile(bootstrap_stats, [alpha / 2, 1 - alpha / 2])
    return left, right


n = 1000
B = 10000
alpha = 0.05

np.random.seed(42)
values_a = np.random.normal(90, 20, n)
values_b = np.random.normal(90, 15, n)

pe = np.quantile(values_b, 0.9) - np.quantile(values_a, 0.9)

bootstrap_values_a = np.random.choice(values_a, (B, n), True)
bootstrap_metrics_a = np.quantile(bootstrap_values_a, 0.9, axis=1)
bootstrap_values_b = np.random.choice(values_b, (B, n), True)
bootstrap_metrics_b = np.quantile(bootstrap_values_b, 0.9, axis=1)

bootstrap_stats = bootstrap_metrics_b - bootstrap_metrics_a
ci = get_percentile_ci(bootstrap_stats, pe, alpha)
has_effect = not (ci[0] < 0 < ci[1])

# Визуализация
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(bootstrap_stats, bins=50, kde=True)
plt.axvline(pe, color="r", linestyle="--", label=f"Точечная оценка: {pe:.2f}")
plt.axvline(ci[0], color="g", linestyle=":", label=f"ДИ: ({ci[0]:.2f}, {ci[1]:.2f})")
plt.axvline(ci[1], color="g", linestyle=":")
plt.title("Бутстрап-распределение разницы квантилей")
plt.xlabel("Разница 90% квантилей (B - A)")
plt.ylabel("Частота")
plt.legend()

plt.subplot(1, 2, 2)
sns.kdeplot(values_a, label="Выборка A", fill=True)
sns.kdeplot(values_b, label="Выборка B", fill=True)
plt.axvline(np.quantile(values_a, 0.9), color="blue", linestyle="--", alpha=0.5)
plt.axvline(np.quantile(values_b, 0.9), color="orange", linestyle="--", alpha=0.5)
plt.title("Исходные распределения с 90% квантилями")
plt.xlabel("Значения")
plt.ylabel("Плотность")
plt.legend()

plt.tight_layout()
plt.show()

print(f"Значение 90% квантиля изменилось на: {pe:0.2f}")
print(f"{((1 - alpha) * 100)}% доверительный интервал: ({ci[0]:0.2f}, {ci[1]:0.2f})")
print(f"Отличия статистически значимые: {has_effect}")
