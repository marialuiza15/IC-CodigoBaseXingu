import pandas as pd

input_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\data\MAPA DIÁRIO PRODUÇÃO - AGOSTO 2024.csv'
output_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\output\lista_cid_descricao.csv'

cid_descriptions = {
    'A09': 'Diarreia e gastroenterite de origem infecciosa presumível',
    'J00': 'Resfriado comum',
    'R55': 'Síncope e colapso',
    'E86': 'Desidratação',
    'T301': 'Queimadura de primeiro grau',
    'K08.80': 'Odontalgia',
    'Z03': 'Observação por suspeita de doença',
    'B37': 'Candidíase',
    'Z34': 'Gestação de baixo risco',
    'N76.1': 'Vaginose bacteriana',
    'K59': 'Constipação',
    'R73': 'Hiperglicemia',
    'N39.0': 'Infecção urinária',
    'L02': 'Furúnculo',
    'M79.1': 'Mialgia',
    'R10': 'Dor abdominal',
    'K29': 'Gastrite',
    'M75': 'Lesões no ombro',
    'R50.9': 'Febre, não especificada',
    'R11': 'Emese',
    'M54.5': 'Lombalgia',
    'M54.6': 'Dor na coluna',
    'H83': 'Outros transtornos do ouvido interno',
    'H61': 'Outros transtornos do ouvido externo',
    'J11': 'Gripe',
    'L01': 'Impetigo',
    'Z480': 'Curativo',
    'R51': 'Cefaleia',
    'M62.6': 'Distenção muscular',
    'Z76': 'Orientação gerais',
    'H10': 'Conjuntivite',
    'H65': 'Otite',
    'M75.5': 'Bursite',
    'R05': 'Tosse',
}

df = pd.read_csv(input_path, sep=',', encoding='utf-8', skip_blank_lines=True)

col_cid = [col for col in df.columns if col.strip().upper() == 'CID']
if col_cid:
    col_cid = col_cid[0]
else:
    raise Exception('Coluna CID não encontrada.')

ranking = df[col_cid].value_counts().reset_index()
ranking.columns = ['CID', 'FREQUÊNCIA']

ranking['DESCRIÇÃO'] = ranking['CID'].map(cid_descriptions).fillna('Descrição não encontrada')

ranking.to_csv(output_path, index=False, encoding='utf-8')