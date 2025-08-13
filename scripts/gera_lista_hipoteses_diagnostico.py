import pandas as pd

input_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\data\MAPA DIÁRIO PRODUÇÃO - AGOSTO 2024.csv'
output_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\output\lista_hipoteses_diagnostico.csv'

df = pd.read_csv(input_path, sep=',', encoding='utf-8', skip_blank_lines=True)

col_hd = [col for col in df.columns if 'HIPÓTESE DIAGNÓSTICO' in col][0]

ranking = df[col_hd].value_counts().reset_index()
ranking.columns = ['HIPÓTESE DIAGNÓSTICO', 'FREQUÊNCIA']

ranking.to_csv(output_path, index=False, encoding='utf-8')