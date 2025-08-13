# Monitoramento da Saúde Indígena – UBSI Leonardo Villas-Boas

Este projeto tem como objetivo aprimorar o monitoramento da saúde indígena no Território Indígena do Xingu (TIX), utilizando soluções digitais para aumentar a eficiência e a qualidade na coleta, análise e utilização das informações de saúde.

Os dados utilizados foram extraídos da planilha de acompanhamento de atendimentos da Unidade Básica de Saúde Indígena Leonardo Villas-Boas (LV), referentes ao mês de agosto de 2024, abrangendo registros de consultas médicas, atendimentos de enfermagem, procedimentos, notificações e outros serviços prestados à população indígena local.

O processamento dos dados incluiu etapas de tratamento, limpeza e análise realizadas em **Python**, com uso das bibliotecas:
- **pandas** e **numpy** para manipulação e padronização dos dados;
- **openpyxl** para leitura de planilhas Excel;
- **matplotlib** e **seaborn** para geração de visualizações exploratórias.

O projeto também contempla a criação de **dashboards interativos no Looker Studio**, permitindo a apresentação clara e dinâmica de indicadores de saúde para auxiliar a tomada de decisão por parte das equipes de gestão e assistência.

## Estrutura do Projeto
- `scripts/` – Códigos Python para tratamento, análise e visualização de dados.
- `data/` – Planilhas de entrada (não incluídas neste repositório por questões de privacidade).
- `outputs/` – Planilhas de saída (usadas no Looker Studio para visualização)
