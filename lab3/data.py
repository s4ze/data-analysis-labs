import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import pycountry
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

PLOT_LABEL_FONT_SIZE = 14


def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap("hsv", n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS


# Установка размера 2D графика
def set_plot_size(w, h, figure=plt):
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 12
    fig_size[1] = 4.5
    figure.rcParams["figure.figsize"] = fig_size


set_plot_size(12, 4.5)


def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys, values)


df = pd.read_csv("scrubbed.csv", escapechar="`", low_memory=False)

df.fillna(value="unknown")
shapes_label_count = pd.value_counts(df["shape"].values, sort=True)
