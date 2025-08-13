import pandas as pd

input_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\data\MAPA DIÁRIO PRODUÇÃO - AGOSTO 2024.csv'
output_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\output\lista_cid_semana.csv'

df = pd.read_csv(input_path, sep=',', encoding='utf-8', skip_blank_lines=True)

col_data = [col for col in df.columns if 'DATA DO ATENDIMENTO' in col.upper()][0]
col_cid = [col for col in df.columns if col.strip().upper() == 'CID'][0]

df[col_data] = pd.to_datetime(df[col_data], errors='coerce', dayfirst=True)

df = df.dropna(subset=[col_data, col_cid])

df['SEMANA'] = df[col_data].dt.day.apply(lambda d: (d - 1) // 7 + 1)

ranking = df.groupby(['SEMANA', col_cid]).size().reset_index(name='FREQUÊNCIA')

ranking = ranking.sort_values(['SEMANA', 'FREQUÊNCIA'], ascending=[True, False])

ranking.to_csv(output_path, index=False, encoding='utf-8')