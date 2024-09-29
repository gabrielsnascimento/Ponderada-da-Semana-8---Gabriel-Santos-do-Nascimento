import unittest
from sea_level_predictor import *
import test_module

def main():
    # Chama a função principal para executar o código de previsão do nível do mar
    print("Executando a previsão do nível do mar...")
    # Aqui você pode adicionar qualquer lógica adicional que deseje executar.

if __name__ == '__main__':
    main()

    # Executar os testes
    print("Executando os testes...")
    test_suite = unittest.defaultTestLoader.loadTestsFromModule(test_module)
    unittest.TextTestRunner().run(test_suite)
