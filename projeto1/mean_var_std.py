import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("A lista deve conter nove números")
    
    # Converte a lista em uma matriz 3x3
    matrix = np.array(lst).reshape(3, 3)
    
    # Cálculos ao longo do eixo 0 (colunas) e eixo 1 (linhas)
    mean_axis1 = matrix.mean(axis=0).tolist()
    mean_axis2 = matrix.mean(axis=1).tolist()
    mean_flattened = matrix.mean().tolist()
    
    var_axis1 = matrix.var(axis=0).tolist()
    var_axis2 = matrix.var(axis=1).tolist()
    var_flattened = matrix.var().tolist()
    
    std_axis1 = matrix.std(axis=0).tolist()
    std_axis2 = matrix.std(axis=1).tolist()
    std_flattened = matrix.std().tolist()
    
    max_axis1 = matrix.max(axis=0).tolist()
    max_axis2 = matrix.max(axis=1).tolist()
    max_flattened = matrix.max().tolist()
    
    min_axis1 = matrix.min(axis=0).tolist()
    min_axis2 = matrix.min(axis=1).tolist()
    min_flattened = matrix.min().tolist()
    
    sum_axis1 = matrix.sum(axis=0).tolist()
    sum_axis2 = matrix.sum(axis=1).tolist()
    sum_flattened = matrix.sum().tolist()
    
    # Criação do dicionário com todos os resultados
    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [var_axis1, var_axis2, var_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }
    
    return calculations
