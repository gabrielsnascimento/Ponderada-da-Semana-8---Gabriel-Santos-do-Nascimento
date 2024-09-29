import time_series_visualizer as tsv
import unittest
import test_module

# Função principal que executa gráficos e testes
def run_all():
    # Gera os gráficos
    tsv.draw_line_plot()
    tsv.draw_bar_plot()
    tsv.draw_box_plot()

    # Executa os testes
    print("Running tests...")
    unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromModule(test_module))

if __name__ == "__main__":
    run_all()
