import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def obtener_estadisticas_descriptivas(df):
    # Forzamos a que extraiga solo lo numérico
    num = df.describe(include=[float, int])
    # Forzamos a que extraiga solo lo categórico (strings)
    cat = df.describe(include=[object])
    
    return num, cat

def graficar_distribucion_y_outliers(df, columna):
    """
    Crea un histograma y un boxplot para una columna específica.
    """
    # Configuramos el estilo
    sns.set_theme(style="whitegrid")
    
    # Creamos una figura con dos subgráficos
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # 1. Histograma con curva de densidad (KDE)
    sns.histplot(df[columna], kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title(f'Histograma de {columna}')
    
    # 2. Boxplot
    sns.boxplot(x=df[columna], ax=axes[1], color='lightcoral')
    axes[1].set_title(f'Boxplot de {columna}')
    
    plt.tight_layout()
    plt.show()

def graficar_tendencia_temporal(df):
    df_temp = df.copy()
    df_temp['Date'] = pd.to_datetime(df_temp['Date'])
    
    # CAMBIO AQUÍ: Usamos 'ME' en lugar de 'M'
    resumen_mensual = df_temp.resample('ME', on='Date')['Total Amount'].sum()    # Usamos resumen_mensual.index y .values para evitar errores de tipo
    sns.lineplot(x=resumen_mensual.index, y=resumen_mensual.values, marker='o', color='forestgreen')
    
    plt.title('Tendencia Mensual de Ventas (Total Amount)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
    
    return resumen_mensual

def graficar_relacion_variables(df, x_var, y_var):
    """
    Crea un gráfico de dispersión con línea de tendencia para analizar correlaciones.
    """
    plt.figure(figsize=(10, 6))
    
    # Creamos el scatter plot
    sns.regplot(data=df, x=x_var, y=y_var, 
                scatter_kws={'alpha':0.5, 'color':'teal'}, 
                line_kws={'color':'red', 'label':'Tendencia'})
    
    plt.title(f'Análisis de Correlación: {x_var} vs {y_var}', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()
    
    # Retornamos el coeficiente de correlación para el f-string
    return df[x_var].corr(df[y_var])

def graficar_distribucion_y_outliers(df, columna):
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # 1. Histograma
    sns.histplot(df[columna], kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title(f'Histograma de {columna}')
    
    # 2. Boxplot
    sns.boxplot(x=df[columna], ax=axes[1], color='lightcoral')
    axes[1].set_title(f'Boxplot de {columna}')
    
    plt.tight_layout()
    plt.show()
    
    # IMPORTANTE: Debemos retornar el describe() para que el Notebook lo reciba
    return df[columna].describe()