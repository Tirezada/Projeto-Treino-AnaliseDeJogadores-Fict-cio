import pandas as pd

df_stats = pd.read_excel('estatisticas_jogadores.xlsx', sheet_name='Jogadores', header=1, skipfooter=1)


def analise_grupo(coluna, valor):
    return df_stats.groupby(coluna)[valor].sum().sort_values(ascending = False)


colunas = [
    'Jogos', 'Gols', 'Assistências', 'Chutes no Gol',
    'Dribles Certos', 'Cartões Amarelos', 'Min. Jogados',
    'Altura (cm)', 'Peso (kg)' 
]

for col in colunas:
    total = analise_grupo('Posição', col)
    media = (total / df_stats['Posição'].value_counts()).sort_values(ascending=False)
    
    print(f'--- {col} por Posição ---')
    print(total.to_string())
    print(f'--- Média de {col} por Posição ---')
    print(media.to_string())


