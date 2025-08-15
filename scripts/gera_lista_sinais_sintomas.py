import pandas as pd


input_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\data\MAPA DIÁRIO PRODUÇÃO - AGOSTO 2024.csv'
output_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\output\lista_sinais_sintomas.csv'

df = pd.read_csv(input_path, sep=',', encoding='utf-8', skip_blank_lines=True)

col_sinais = [col for col in df.columns if 'SINAIS E SINTOMAS' in col.upper()]
if col_sinais:
    col_sinais = col_sinais[0]
else:
    raise Exception('Coluna SINAIS E SINTOMAS não encontrada.')

sintomas = df[col_sinais].dropna().str.split(',')
sintomas_flat = [s.strip().upper() for sublist in sintomas for s in sublist if s.strip()]

ranking = pd.Series(sintomas_flat).value_counts().reset_index()
ranking.columns = ['SINAL OU SINTOMA', 'FREQUÊNCIA']

ranking.to_csv(output_path, index=False, encoding='utf-8')