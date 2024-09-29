import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importar dados
df = pd.read_csv("medical_examination.csv")

# 1. Adicionar coluna 'sobrepeso'
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop(columns=['BMI'], inplace=True)

# 2. Normalizar dados fazendo 0 sempre bom e 1 sempre ruim
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 3. Desenhar gráfico categórico
def draw_cat_plot():
    # 3.1 Criar DataFrame para o gráfico categórico usando `pd.melt`
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 3.2 Agrupar e reformular os dados para separá-los por 'cardio'
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

    # 3.3 Desenhar o gráfico categórico com 'sns.catplot()'
    fig = sns.catplot(x='variable', y='size', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # Retornar a figura
    return fig

# 4. Desenhar mapa de calor
def draw_heat_map():
    # 4.1 Limpar os dados
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 4.2 Calcular a matriz de correlação
    corr = df_heat.corr()

    # 4.3 Gerar uma máscara para o triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 4.4 Configurar a figura do matplotlib
    fig, ax = plt.subplots(figsize=(12, 8))

    # 4.5 Desenhar o mapa de calor
    sns.heatmap(corr, annot=True, mask=mask, cmap='coolwarm', square=True, linewidths=0.5, ax=ax)

    # Retornar a figura
    return fig
