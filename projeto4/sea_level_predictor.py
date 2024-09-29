import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Importar os dados
df = pd.read_csv('epa-sea-level.csv')

# Criar um gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label="Original Data")

# Linha de melhor ajuste para todos os dados
slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series([i for i in range(1880, 2051)])
sea_level_predicted_all = intercept_all + slope_all * years_extended
plt.plot(years_extended, sea_level_predicted_all, 'r', label='Best fit line (1880-2050)')

# Linha de melhor ajuste para dados de 2000 em diante
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_recent = pd.Series([i for i in range(2000, 2051)])
sea_level_predicted_recent = intercept_recent + slope_recent * years_recent
plt.plot(years_recent, sea_level_predicted_recent, 'green', label='Best fit line (2000-2050)')

# Configurações de rótulos e título
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Salvar gráfico como .png
plt.savefig('sea_level_plot.png')

# Exibir o gráfico
plt.show()
