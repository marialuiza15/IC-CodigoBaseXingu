import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

selected_cols = ['CID', 'HIPÓTESE DIAGNÓSTICO  -  HD', 'SINAIS E SINTOMAS']
filename_suffix = "cid_hd_sintomas"

input_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\data\MAPA DIÁRIO PRODUÇÃO - AGOSTO 2024.csv'
output_path = r'C:\Users\maria\OneDrive\Desktop\IC\IC-CodigoBaseXingu\output\lista_apriori_trios_frequentes.csv'

df = pd.read_csv(input_path)
df_selected = df[selected_cols].dropna(how='all').fillna("")

def extract_items(row):
    items = []
    for col in selected_cols:
        parts = [item.strip().upper() for item in row[col].split(',') if item.strip()]
        items.extend(parts)
    return list(set(items))

transactions = df_selected.apply(extract_items, axis=1).tolist()

te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_array, columns=te.columns_)

frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
frequent_itemsets["Frequência (%)"] = (frequent_itemsets["support"] * 100).round(2)

itemsets_trios = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: len(x) == 3)]
itemsets_trios = itemsets_trios.sort_values(by="Frequência (%)", ascending=False)

itemsets_trios_split = itemsets_trios.copy()
itemsets_trios_split[['Item 1', 'Item 2', 'Item 3']] = itemsets_trios_split['itemsets'].apply(lambda x: pd.Series(list(x)))

itemsets_trios_split[['Item 1', 'Item 2', 'Item 3', 'Frequência (%)']].to_csv(output_path, index=False, encoding='utf-8-sig')