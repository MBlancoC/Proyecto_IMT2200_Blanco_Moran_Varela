import matplotlib.pyplot as plt
import seaborn as sns

def plot_hist(dataframe, variable):
    
    g = sns.displot(x = variable, data = dataframe, kde = True) # Histograma
    g.fig.suptitle(f'Histograma {variable}', y = 1.05)
    media = round(dataframe[variable].mean(), 1)
    mediana = round(dataframe[variable].median(), 1)

    plt.axvline(media, lw = 2, color = 'g', linestyle = '--', label = f'media = {media}')
    plt.axvline(mediana, lw = 2, color = 'r', linestyle = '--', label = f'mediana = {mediana}')
    plt.legend(loc="upper right")
    
def frecuencia(data,variable):
    print(round(data[variable].value_counts('%')*100, 2))

def graf_barra(dataframe, variable):
    
    hue_colors = {1: 'red',
             2: 'yellow',
             3: 'blue',
             4: 'green',
             5: 'white'}
    sns.catplot(x = variable, data = dataframe, kind = 'count', order = dataframe[variable].value_counts().index)
    plt.show()  