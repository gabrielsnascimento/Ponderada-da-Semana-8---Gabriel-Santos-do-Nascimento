import unittest
import os
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class MedicalDataVisualizerTests(unittest.TestCase):
    def setUp(self):
        # Executar as funções para gerar os gráficos
        self.catplot_fig = draw_cat_plot()
        self.heatmap_fig = draw_heat_map()

    def test_cat_plot(self):
        # Testar se o arquivo da figura categórica foi criado
        self.catplot_fig.savefig('catplot.png')
        self.assertTrue(os.path.exists('catplot.png'), "Cat plot image was not created.")

    def test_heat_map(self):
        # Testar se o arquivo do heatmap foi criado
        self.heatmap_fig.savefig('heatmap.png')
        self.assertTrue(os.path.exists('heatmap.png'), "Heatmap image was not created.")

if __name__ == "__main__":
    unittest.main()
