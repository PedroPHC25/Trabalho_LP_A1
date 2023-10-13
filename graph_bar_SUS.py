import pandas as pd
import matplotlib.pyplot as plt
from df_concatenator import data
import numpy as np

def graph_SUS(df, y1, y2, y3, title, image_graph_name, legend = ["Hospital Filantrópico", "Hospital Privado", "Hospital Público"], width = 0.2, colors = ['royalblue', 'lightseagreen', 'mediumpurple']):
    x = np.arange(len(df))
    plt.figure(figsize = (10, 6))
    plt.title(title, fontsize = 16)
    plt.bar(x - width, y1, width, color=colors[0])
    plt.bar(x, y2, width, color=colors[1])
    plt.bar(x + width, y3, width, color=colors[2])
    plt.xticks(x, df["Estado"]) 
    plt.legend(legend) 
    plt.savefig(f"graphs/{image_graph_name}")
    plt.show()