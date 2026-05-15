import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def obtener_estadisticas_descriptivas(df):
    """
    Despliega estadísticas descriptivas de variables numéricas y categóricas
    """
    # Extraer variables numéricas
    num = df.describe(include=[float, int])
    # Extraer varibles en "strings"
    cat = df.describe(include=[object])
    
    return num, cat

def graficar_distribucion_y_outliers(df, columna):
    """
    Crea un histograma y un boxplot para una columna específica.
    """
    # Estilo
    sns.set_theme(style="whitegrid")
    
    # Crear figura con dos subgráficos
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Histograma con curva de densidad (KDE)
    sns.histplot(df[columna], kde=True, ax=axes[0], color='plum')
    axes[0].set_title(f'Histograma de {columna}')
    
    # Boxplot
    sns.boxplot(x=df[columna], ax=axes[1], color='plum')
    axes[1].set_title(f'Boxplot de {columna}')
    
    plt.tight_layout() # Distribuir y acomodar espacio
    plt.show()

def graficar_tendencia_temporal(df):
    """
    Crea un gráfico de línea
    """
    df_temp = df.copy()
    df_temp['Date'] = pd.to_datetime(df_temp['Date']) # Formato fecha específico
    
    resumen_mensual = df_temp.resample('ME', on='Date')['Total Amount'].sum()    # Resumen_mensual.index y .values para evitar errores de tipo
    sns.lineplot(x=resumen_mensual.index, y=resumen_mensual.values, marker='o', color='#1B998B')
    
    plt.title('Tendencia Mensual de Ventas (Total Amount)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
    return resumen_mensual

def graficar_relacion_variables(df, x_var, y_var):
    """
    Crea un gráfico de dispersión con línea de tendencia para analizar correlaciones.
    """
    plt.figure(figsize=(10, 6))
    
    # Creamos el scatter plot
    sns.regplot(data=df, x=x_var, y=y_var, scatter_kws={'alpha':0.5, 'color':'teal'}, line_kws={'color':'#ED217C', 'label':'Tendencia'})
    
    plt.title(f'Análisis de Correlación: {x_var} vs {y_var}', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(loc='upper right', frameon=True, shadow=True, borderpad=1)
    plt.show()
    
    # Retornar coeficiente de correlación
    return df[x_var].corr(df[y_var])

def graficar_distribucion_y_outliers(df, columna):
    """
    Crea un histograma para ver distribución y un boxplot para outliers
    """
    # Crear figura con dos subgráficos
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    
    # Histograma
    sns.histplot(df[columna], kde=True, ax=axes[0], color='skyblue')
    axes[0].set_title(f'Histograma de {columna}')
    
    # Boxplot
    sns.boxplot(x=df[columna], ax=axes[1], color='plum')
    axes[1].set_title(f'Boxplot de {columna}')
    
    plt.tight_layout() # Distribuye y ordena espacio
    plt.show()
    
    return df[columna].describe()