import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

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

def report_scores(y_testeo, y_prediccion):
    mse = mean_squared_error(y_testeo, y_prediccion).round(1)
    r2 = r2_score(y_testeo, y_prediccion).round(2)
    
    print('Error Cuadrático Promedio (MSE):', mse)
    print('R2:', r2) 

def fetch_features(dataframe, variable_objetivo):
    columns = dataframe
    nombre_var =[]
    pearson_corr =[]
    abs_pearson_corr = []
    for col in columns:
        if col != variable_objetivo:
            nombre_var.append(col)
            pearson_corr.append(dataframe[col].corr(dataframe[variable_objetivo]))
            abs_pearson_corr.append(abs(dataframe[col].corr(dataframe[variable_objetivo])))
            
    features = pd.DataFrame({'variables': nombre_var, 'correlaciones': pearson_corr, 'abs_corr': abs_pearson_corr})
    features2 = features.set_index('variables')
    features3= features2.sort_values(by = ['abs_corr'], ascending = False)
    return features3