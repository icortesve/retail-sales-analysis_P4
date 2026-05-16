import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def analisis_correlacion(df):
    """Genera un mapa de calor para identificar relaciones multivariables."""
    # Crear canvas
    plt.figure(figsize=(10, 8))

    # Para la matriz, se seleccionan solo las variables numéricas
    corr = df.select_dtypes(include=[np.number]).corr()
    
    sns.heatmap(corr, annot=True, cmap='vlag', fmt=".2f", linewidths=0.5)
    plt.title('Mapa de Calor: Correlaciones de Variables', fontsize=15, pad=20)
    plt.show()

def graficar_comparativa_avanzada(df):
    """Crea subplots para comparar Género y Categoría de Producto respecto a ventas."""

    # Crear Canvas doble
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Subplot 1 (axes[0]): Ventas totales acumuladas por Género
    sns.barplot(data=df, x='Gender', y='Total Amount', ax=axes[0], 
                palette='viridis', hue='Gender', legend=False, estimator=sum) # 'estimator=sum' suma todos los valores de cada categoría (Male y Female)
    # Diseño
    axes[0].set_title('Ventas Totales por Género', fontsize=13)
    axes[0].set_xlabel('Género')
    axes[0].set_ylabel('Monto Total ($)')
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)
    
    # Subplot 2 (axes[1]): Ventas totales acumuladas por Categoría de Producto
    sns.barplot(data=df, x='Product Category', y='Total Amount', ax=axes[1], 
                palette='magma', hue='Product Category', legend=False, estimator=sum)
    # Diseño
    axes[1].set_title('Ventas Totales por Categoría de Producto', fontsize=13)
    axes[1].set_xlabel('Categoría')
    axes[1].set_ylabel('Monto Total ($)')
    axes[1].grid(axis='y', linestyle='--', alpha=0.8) # axis='y' --> orientación delaslíneas de cuadrícula
    
    plt.tight_layout() # Distribuye y ordena el espacio
    plt.show()

def graficar_tendencia_anotada(df):
    """Gráfico de tendencia temporal"""

    # Copia de seguridad
    df_temp = df.copy()
    # Fecha en formato fecha
    df_temp['Date'] = pd.to_datetime(df_temp['Date'])
    
    # Resample mensual usando 'ME' (Month End) para evitar el Warning de pandas
    resumen = df_temp.resample('ME', on='Date')['Total Amount'].sum()
    
    # Crear canvas
    plt.figure(figsize=(12, 6))
    plt.plot(resumen.index, resumen.values, marker='s', color='#E63946', linewidth=2, label='Ventas Mensuales')
    
    # Localizar punto máximo automáticamente para la anotación
    max_val = resumen.max()
    max_date = resumen.idxmax()
    
    # Agregar anotación
    plt.annotate(f'Máximo Histórico\n${max_val:,.2f}', # anotación en pantalla
                 xy=(max_date, max_val), # coordenadas (punto máx)
                 xytext=(max_date + pd.Timedelta(days=25), max_val * 0.93), # Posición de la caja de texto (levemente desplazada)
                 arrowprops=dict(facecolor='black', shrink=0.08, width=2, headwidth=7),# Diseño y proporciones geométricas de la flecha
                 fontsize=11, fontweight='bold', color='darkred', # Diseño fuente
                 bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3)) # caja de texto con especificaciones de diseño
    
    # Diseño Gráfico
    plt.title('Tendencia Temporal de Ventas con Identificación de Hitos', fontsize=14, pad=15)
    plt.xlabel('Fecha de Registro')
    plt.ylabel('Monto Total Acumulado ($)')
    plt.grid(True, which='both', linestyle=':', alpha=0.6)
    plt.legend(loc='upper left', frameon=True)
    plt.show()