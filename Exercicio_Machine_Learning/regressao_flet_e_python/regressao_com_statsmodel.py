# This code snippet is a Python script that demonstrates reading a CSV file using pandas, handling
# specific exceptions related to file reading and data parsing, and then printing out the dimensions
# of the loaded DataFrame. Here's a breakdown of what the code does:
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import scipy.stats as stats
import seaborn as sns



file_path = "Exercicio_Machine_Learning/regressao_flet_e_python/mt_cars.csv"

if file_path:
    try:
        base = pd.read_csv(file_path, encoding='latin-1')
        print("Dimensões do DataFrame:", base.shape)  # Imprime as dimensões corretamente
        # Agora você pode continuar com a análise dos dados em 'base'
        # Exemplo de acesso a uma coluna: print(base["nome_da_coluna"].head())
        print(base.head())
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{file_path}'")
    except pd.errors.EmptyDataError:
        print(f"Erro: Arquivo CSV está vazio em '{file_path}'")
    except pd.errors.ParserError:
        print(f"Erro: Erro ao analisar o arquivo CSV em '{file_path}'")
    except Exception as e: # Captura qualquer outro erro
        print(f"Erro inesperado: {e}")
else:    
    print("Nenhum arquivo selecionado.")
    
