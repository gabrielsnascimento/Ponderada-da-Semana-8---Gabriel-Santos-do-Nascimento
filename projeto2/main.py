# main.py

# Este script serve para rodar as funções e gerar as figuras

from medical_data_visualizer import draw_cat_plot, draw_heat_map
import unittest
import test_module

# Testar o código (opcional)
if __name__ == "__main__":
    # Desenhar e salvar a figura categórica
    cat_plot_fig = draw_cat_plot()
    cat_plot_fig.savefig('catplot.png')

    # Desenhar e salvar o mapa de calor
    heat_map_fig = draw_heat_map()
    heat_map_fig.savefig('heatmap.png')

    # Rodar os testes unitários
    unittest.main(module=test_module, exit=False)
