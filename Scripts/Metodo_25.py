# %% [markdown]
# # @FutPythonTrader

# %%
import pandas as pd
import numpy as np
#import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

def dia():
    from datetime import date, timedelta
    dia = date.today() + timedelta(0)
    return dia

def drop_reset_index(df):
    df = df.dropna()
    df = df.reset_index(drop=True)
    df.index += 1
    return df
    
def grafico(df, nome):
    df = df.reset_index(drop=True)
    df.index += 1
    df['Profit_acu'] = df.Profit.cumsum()
    profit = round(df.Profit_acu.tail(1).item(),2)
    ROI = round((df.Profit_acu.tail(1)/len(df)*100).item(),2)
    df.Profit_acu.plot(title=nome, xlabel='Entradas', ylabel='Stakes')
    print("Profit:",profit,"stakes em", len(df),"jogos")
    print("ROI:",ROI,"%")

# %% [markdown]
# # Importando a Base de Dados

# %%

# df1 = pd.read_excel("G:\\Meu Drive\\Programacao\\futPythonTrader\\BasesDeDados\\x_FutPythonTrader_Base_de_Dados_Temporada_2122_x.xlsx")
# df2 = pd.read_excel("https://github.com/futpythontrader/YouTube/raw/main/x_FutPythonTrader_Base_de_Dados_Temporada_Atual_x.xlsx")


# df = pd.concat([df1,df2])
# df.reset_index(inplace=True, drop=True)
# df.index = df.index.set_names(['Nº'])
# df = df.rename(index=lambda x: x + 1)

# df = df[['Date','League','Home','Away','Season','FT_Goals_H','FT_Goals_A','FT_Odds_H','FT_Odds_D','FT_Odds_A','FT_Odds_Over25','FT_Odds_Under25','Odds_BTTS_Yes','Odds_BTTS_No']]

#df

# %%
# flt = ((df.FT_Odds_H != 0) & (df.FT_Odds_D != 0) & (df.FT_Odds_A != 0))
# df = df[flt]

# #somandos os gols do jogo para chegar no total
# df["Total_Goals_FT"] = df["FT_Goals_H"] + df["FT_Goals_A"]

# #verificando qual o resultado das partidas
# df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'FT_Result'] = "H"
# df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'FT_Result'] = "D"
# df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'FT_Result'] = "A"

# #verificando se foi btts sim ou nao e preenchendo a coluna ft_btts
# # df.loc[(df['FT_Goals_H'] > 0) & (df['FT_Goals_A'] > 0), 'BTTS'] = "S"
# # df.loc[(df['FT_Goals_H'] > 0) & (df['FT_Goals_A'] < 1), 'BTTS'] = "N"
# # df.loc[(df['FT_Goals_H'] < 1) & (df['FT_Goals_A'] > 0), 'BTTS'] = "N"
# # df.loc[(df['FT_Goals_H'] < 1) & (df['FT_Goals_A'] < 1), 'BTTS'] = "N"

# df['BTTS'] = df.apply(lambda row: 1 if (row['FT_Goals_H'] > 0 and row['FT_Goals_A'] > 0) else 0, axis=1) 

# #verificando quais jogos tiveram over 2.5
# df['Over25_FT'] = df.apply(lambda row: 1 if (row['Total_Goals_FT'] > 2) else 0, axis=1)

# #verificando a porcetagem de 2.5 de 5 em 5 partidas
# df['Porc_Over25FT_Home'] = (df.groupby('Home')['Over25_FT'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True) * 100).shift(1)
# df['Porc_Over25FT_Away'] = (df.groupby('Away')['Over25_FT'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True) * 100).shift(1)

# #verificando a porcetagem de btts de 5 em 5 partidas
# df['Porc_BTTS_Home'] = (df.groupby('Home')['BTTS'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True) * 100).shift(1)
# df['Porc_BTTS_Away'] = (df.groupby('Away')['BTTS'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True) * 100).shift(1)

# # Médias, Desvio Padrão e Coeficiente de Variação

# df['Media_Gols_Feitos_Home'] = df.groupby('Home')['FT_Goals_H'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True).shift(1)
# df['Media_Gols_Sofridos_Home'] = df.groupby('Home')['FT_Goals_A'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True).shift(1)

# df['Media_Gols_Feitos_Away'] = df.groupby('Away')['FT_Goals_A'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True).shift(1)
# df['Media_Gols_Sofridos_Away'] = df.groupby('Away')['FT_Goals_H'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True).shift(1)

# df['DP_Gols_Feitos_Home'] = df.groupby('Home')['FT_Goals_H'].rolling(window=5, min_periods=1).std().reset_index(0,drop=True).shift(1)
# df['DP_Gols_Sofridos_Home'] = df.groupby('Home')['FT_Goals_A'].rolling(window=5, min_periods=1).std().reset_index(0,drop=True).shift(1)

# df['DP_Gols_Feitos_Away'] = df.groupby('Away')['FT_Goals_A'].rolling(window=5, min_periods=1).std().reset_index(0,drop=True).shift(1)
# df['DP_Gols_Sofridos_Away'] = df.groupby('Away')['FT_Goals_H'].rolling(window=5, min_periods=1).std().reset_index(0,drop=True).shift(1)

# df['CV_Gols_Feitos_Home'] = (df['DP_Gols_Feitos_Home'] / df['Media_Gols_Feitos_Home']).shift(1)
# df['CV_Gols_Sofridos_Home'] = (df['DP_Gols_Sofridos_Home'] / df['Media_Gols_Sofridos_Home']).shift(1)

# df['CV_Gols_Feitos_Away'] = (df['DP_Gols_Feitos_Away'] / df['Media_Gols_Feitos_Away']).shift(1)
# df['CV_Gols_Sofridos_Away'] = (df['DP_Gols_Sofridos_Away'] / df['Media_Gols_Sofridos_Away']).shift(1)

# # Profit

# Stake = 1
# green = Stake * (df.FT_Odds_Over25 - 1) 
# red = -Stake

# df.loc[df['Over25_FT'] == 1, 'Profit'] = green
# df.loc[df['Over25_FT'] == 0, 'Profit'] = red

# #porcentagem dos gols

# # Probabilidades
# df['p_H'] = 1 / df.FT_Odds_H
# df['p_D'] = 1 / df.FT_Odds_D
# df['p_A'] = 1 / df.FT_Odds_A

# # CV das Odds do Match Odds
# df['CV_HDA'] = df[['p_H','p_D','p_A']].std(ddof=0, axis=1) / df[['p_H','p_D','p_A']].mean(axis=1)


# # Valor do Gol
# df['VG_H'] = df.FT_Goals_H * df.p_A
# df['VG_A'] = df.FT_Goals_A * df.p_H

# df['Media_VG_H'] = df.groupby('Home')['VG_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
# df['Media_VG_A'] = df.groupby('Away')['VG_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

# df['Media_VG_H'] = df.groupby('Home')['Media_VG_H'].shift(1)
# df['Media_VG_A'] = df.groupby('Away')['Media_VG_A'].shift(1)

# df['DesvPad_VG_H'] = df.groupby('Home')['VG_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
# df['DesvPad_VG_A'] = df.groupby('Away')['VG_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

# df['DesvPad_VG_H'] = df.groupby('Home')['DesvPad_VG_H'].shift(1)
# df['DesvPad_VG_A'] = df.groupby('Away')['DesvPad_VG_A'].shift(1)

# df['CV_VG_H'] = df['DesvPad_VG_H'] / df['Media_VG_H']
# df['CV_VG_A'] = df['DesvPad_VG_A'] / df['Media_VG_A']

# # Custo do Gol
# df['CG_H'] = df.p_H / df.FT_Goals_H
# df['CG_A'] = df.p_A / df.FT_Goals_A

# df['Media_CG_H'] = df.groupby('Home')['CG_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
# df['Media_CG_A'] = df.groupby('Away')['CG_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

# df['Media_CG_H'] = df.groupby('Home')['Media_CG_H'].shift(1)
# df['Media_CG_A'] = df.groupby('Away')['Media_CG_A'].shift(1)

# df['DesvPad_CG_H'] = df.groupby('Home')['CG_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
# df['DesvPad_CG_A'] = df.groupby('Away')['CG_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

# df['DesvPad_CG_H'] = df.groupby('Home')['DesvPad_CG_H'].shift(1)
# df['DesvPad_CG_A'] = df.groupby('Away')['DesvPad_CG_A'].shift(1)

# df['CV_CG_H'] = df['DesvPad_CG_H'] / df['Media_CG_H']
# df['CV_CG_A'] = df['DesvPad_CG_A'] / df['Media_CG_A']

# df.replace(np.inf, 1, inplace=True)
# df = drop_reset_index(df)

# df = df.drop(['VG_H', 'VG_A', 'CG_H', 'CG_A'], axis=1)
# #df.to_excel(f'teste_btts_sim_2.xlsx', index=None)
# df

# %% [markdown]
# # Filtros do Método

# %%
# flt = (
# ((df.FT_Odds_Over25 >= 1.8)) & ((df.FT_Odds_Over25 <= 3))
# & ((df.FT_Odds_H >= 1)) & ((df.FT_Odds_H <= 4))
# & ((df.Porc_Over25FT_Home >= 50))
# & ((df.Porc_BTTS_Away >= 50))
# & ((df.Media_Gols_Sofridos_Home >= 0.5)) & ((df.Media_Gols_Sofridos_Home <= 3))
# & ((df.CV_Gols_Sofridos_Away >= 0.3)) & ((df.CV_Gols_Sofridos_Away <= 0.8))
# & ((df.CV_Gols_Feitos_Away >= 0.5)) & ((df.CV_Gols_Feitos_Away <= 1.6))
# & ((df.CV_Gols_Feitos_Home <= 1.6))
# )


# df = df[df['League'].isin(["Argentina Prim B Nacional",
# "Argentina Primera División",
# "Australia A-League",
# "Austria 2. Liga",
# "Brazil Serie A",
# "Brazil Serie C",
# "Chile Primera B",
# "Chile Segunda División",
# "China Chinese Super League",
# "Czech Republic First League",
# "Ecuador Primera Categoría Serie A",
# "Egypt Egyptian Premier League",
# "England Championship",
# "Finland Veikkausliiga",
# "France Ligue 1",
# "Germany 2. Bundesliga",
# "Germany 3. Liga",
# "Japan J1 League",
# "Japan J2 League",
# "Netherlands Eredivisie",
# "Netherlands Tweede Divisie",
# "Paraguay Division Profesional",
# "Peru Primera División",
# "Poland Ekstraklasa",
# "Republic of Ireland Premier Division",
# "Romania Liga I",
# "Russia Russian Premier League",
# "South Korea K League 1",
# "Spain Segunda División",
# "Sweden Superettan",
# "Switzerland Challenge League",
# "Turkey Süper Lig",
# "Ukraine Ukrainian Premier League",
# "USA MLS",
# "USA USL Championship"
# ]) == True]
# df0 = df[flt]
# grafico(df0,'BTTS sim')

# %% [markdown]
# # Unindo a Base de Dados com os Jogos do Dia

# %%
#df0['League'].unique()

# %%

df1 = pd.read_excel("G:\\Meu Drive\\Programacao\\futPythonTrader\\BasesDeDados\\x_FutPythonTrader_Base_de_Dados_Temporada_2122_x.xlsx")
df2 = pd.read_excel("https://github.com/futpythontrader/YouTube/raw/main/x_FutPythonTrader_Base_de_Dados_Temporada_Atual_x.xlsx")
base = pd.concat([df1,df2])
base.reset_index(inplace=True, drop=True)
base.index = base.index.set_names(['Nº'])
base = base.rename(index=lambda x: x + 1)

base = base[['Date','League','Home','Away','Season','FT_Goals_H','FT_Goals_A','FT_Odds_H','FT_Odds_D','FT_Odds_A','FT_Odds_Over25','FT_Odds_Under25','Odds_BTTS_Yes','Odds_BTTS_No']]
base["Date"] = pd.to_datetime(base["Date"])


# %%
#base['League'].unique()

# %%
base = base[base['League'].isin(["Argentina Prim B Nacional",
"Argentina Primera División",
"Australia A-League",
"Austria 2. Liga",
"Brazil Serie A",
"Brazil Serie C",
"Chile Primera B",
"Chile Segunda División",
"China Chinese Super League",
"Czech Republic First League",
"Ecuador Primera Categoría Serie A",
"Egypt Egyptian Premier League",
"England Championship",
"Finland Veikkausliiga",
"France Ligue 1",
"Germany 2. Bundesliga",
"Germany 3. Liga",
"Japan J1 League",
"Japan J2 League",
"Netherlands Eredivisie",
"Netherlands Tweede Divisie",
"Paraguay Division Profesional",
"Peru Primera División",
"Poland Ekstraklasa",
"Republic of Ireland Premier Division",
"Romania Liga I",
"Russia Russian Premier League",
"South Korea K League 1",
"Spain Segunda División",
"Sweden Superettan",
"Switzerland Challenge League",
"Turkey Süper Lig",
"Ukraine Ukrainian Premier League",
"USA MLS",
"USA USL Championship"]) == True]

# %%
flt = ((base.FT_Odds_H != 0) & (base.FT_Odds_D != 0) & (base.FT_Odds_A != 0))
base = base[flt]

#somandos os gols do jogo para chegar no total
base["Total_Goals_FT"] = base["FT_Goals_H"] + base["FT_Goals_A"]

#verificando qual o resultado das partidas
base.loc[base['FT_Goals_H'] > base['FT_Goals_A'], 'FT_Result'] = "H"
base.loc[base['FT_Goals_H'] == base['FT_Goals_A'], 'FT_Result'] = "D"
base.loc[base['FT_Goals_H'] < base['FT_Goals_A'], 'FT_Result'] = "A"

#verificando se foi btts sim ou nao e preenchendo a coluna ft_btts
# base.loc[(base['FT_Goals_H'] > 0) & (base['FT_Goals_A'] > 0), 'BTTS'] = "S"
# base.loc[(base['FT_Goals_H'] > 0) & (base['FT_Goals_A'] < 1), 'BTTS'] = "N"
# base.loc[(base['FT_Goals_H'] < 1) & (base['FT_Goals_A'] > 0), 'BTTS'] = "N"
# base.loc[(base['FT_Goals_H'] < 1) & (base['FT_Goals_A'] < 1), 'BTTS'] = "N"

base['BTTS'] = base.apply(lambda row: 1 if (row['FT_Goals_H'] > 0 and row['FT_Goals_A'] > 0) else 0, axis=1) 

#verificando quais jogos tiveram over 2.5
base['Over25_FT'] = base.apply(lambda row: 1 if (row['Total_Goals_FT'] > 2) else 0, axis=1)

#verificando a porcetagem de 2.5 de 5 em 5 partidas
base['Porc_Over25FT_Home'] = (base.groupby('Home')['Over25_FT'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True) * 100).shift(1)
base['Porc_Over25FT_Away'] = (base.groupby('Away')['Over25_FT'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True) * 100).shift(1)

#verificando a porcetagem de btts de 5 em 5 partidas
base['Porc_BTTS_Home'] = (base.groupby('Home')['BTTS'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True) * 100).shift(1)
base['Porc_BTTS_Away'] = (base.groupby('Away')['BTTS'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True) * 100).shift(1)

# Médias, Desvio Padrão e Coeficiente de Variação

base['Media_Gols_Feitos_Home'] = base.groupby('Home')['FT_Goals_H'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True).shift(1)
base['Media_Gols_Sofridos_Home'] = base.groupby('Home')['FT_Goals_A'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True).shift(1)

base['Media_Gols_Feitos_Away'] = base.groupby('Away')['FT_Goals_A'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True).shift(1)
base['Media_Gols_Sofridos_Away'] = base.groupby('Away')['FT_Goals_H'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True).shift(1)

base['DP_Gols_Feitos_Home'] = base.groupby('Home')['FT_Goals_H'].rolling(window=5, min_periods=1).std().reset_index(0,drop=True).shift(1)
base['DP_Gols_Sofridos_Home'] = base.groupby('Home')['FT_Goals_A'].rolling(window=5, min_periods=1).std().reset_index(0,drop=True).shift(1)

base['DP_Gols_Feitos_Away'] = base.groupby('Away')['FT_Goals_A'].rolling(window=5, min_periods=1).std().reset_index(0,drop=True).shift(1)
base['DP_Gols_Sofridos_Away'] = base.groupby('Away')['FT_Goals_H'].rolling(window=5, min_periods=1).std().reset_index(0,drop=True).shift(1)

base['CV_Gols_Feitos_Home'] = (base['DP_Gols_Feitos_Home'] / base['Media_Gols_Feitos_Home']).shift(1)
base['CV_Gols_Sofridos_Home'] = (base['DP_Gols_Sofridos_Home'] / base['Media_Gols_Sofridos_Home']).shift(1)

base['CV_Gols_Feitos_Away'] = (base['DP_Gols_Feitos_Away'] / base['Media_Gols_Feitos_Away']).shift(1)
base['CV_Gols_Sofridos_Away'] = (base['DP_Gols_Sofridos_Away'] / base['Media_Gols_Sofridos_Away']).shift(1)

# Profit
green = base.Odds_BTTS_Yes - 1
red = -1

Stake = 1
green = Stake * (base.Odds_BTTS_Yes - 1) 
red = -Stake

base.loc[base['BTTS'] == 1, 'Profit'] = green
base.loc[base['BTTS'] == 0, 'Profit'] = red

#porcentagem dos gols

# Probabilidades
base['p_H'] = 1 / base.FT_Odds_H
base['p_D'] = 1 / base.FT_Odds_D
base['p_A'] = 1 / base.FT_Odds_A

# CV das Odds do Match Odds
base['CV_HDA'] = base[['p_H','p_D','p_A']].std(ddof=0, axis=1) / base[['p_H','p_D','p_A']].mean(axis=1)


# Valor do Gol
base['VG_H'] = base.FT_Goals_H * base.p_A
base['VG_A'] = base.FT_Goals_A * base.p_H

base['Media_VG_H'] = base.groupby('Home')['VG_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
base['Media_VG_A'] = base.groupby('Away')['VG_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

base['Media_VG_H'] = base.groupby('Home')['Media_VG_H'].shift(1)
base['Media_VG_A'] = base.groupby('Away')['Media_VG_A'].shift(1)

base['DesvPad_VG_H'] = base.groupby('Home')['VG_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
base['DesvPad_VG_A'] = base.groupby('Away')['VG_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

base['DesvPad_VG_H'] = base.groupby('Home')['DesvPad_VG_H'].shift(1)
base['DesvPad_VG_A'] = base.groupby('Away')['DesvPad_VG_A'].shift(1)

base['CV_VG_H'] = base['DesvPad_VG_H'] / base['Media_VG_H']
base['CV_VG_A'] = base['DesvPad_VG_A'] / base['Media_VG_A']

# Custo do Gol
base['CG_H'] = base.p_H / base.FT_Goals_H
base['CG_A'] = base.p_A / base.FT_Goals_A

base['Media_CG_H'] = base.groupby('Home')['CG_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
base['Media_CG_A'] = base.groupby('Away')['CG_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

base['Media_CG_H'] = base.groupby('Home')['Media_CG_H'].shift(1)
base['Media_CG_A'] = base.groupby('Away')['Media_CG_A'].shift(1)

base['DesvPad_CG_H'] = base.groupby('Home')['CG_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
base['DesvPad_CG_A'] = base.groupby('Away')['CG_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

base['DesvPad_CG_H'] = base.groupby('Home')['DesvPad_CG_H'].shift(1)
base['DesvPad_CG_A'] = base.groupby('Away')['DesvPad_CG_A'].shift(1)

base['CV_CG_H'] = base['DesvPad_CG_H'] / base['Media_CG_H']
base['CV_CG_A'] = base['DesvPad_CG_A'] / base['Media_CG_A']

base.replace(np.inf, 1, inplace=True)
base = drop_reset_index(base)

base = base.drop(['VG_H', 'VG_A', 'CG_H', 'CG_A'], axis=1)
#base.to_excel(f'teste_btts_sim_2.xlsx', index=None)
#base

# %%
base = drop_reset_index(base)
#base

# %%
#base.columns.to_list()

# %%
#base_H = base[['Home', 'Media_Ptos_H', 'DesvPad_Ptos_H', 'CV_Ptos_H', 'Media_VG_H', 'DesvPad_VG_H', 'CV_VG_H', 'Media_CG_H', 'DesvPad_CG_H', 'CV_CG_H']]

base_H = base[['Home', 'Porc_Over25FT_Home', 'Media_Gols_Sofridos_Home','CV_Gols_Feitos_Home']]

base_A = base[['Away', 'Porc_BTTS_Away', 'CV_Gols_Sofridos_Away','CV_Gols_Feitos_Away']]

#base_H.to_excel('baseh.xlsx', index=None)

# %%
from datetime import date, datetime, timedelta
dia = date.today() - timedelta(-1)
print(dia)

# %%
#jogos_do_dia = pd.read_csv('https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/'+str(dia)+'_Jogos_do_Dia_FlashScore.csv?raw=true')
jogos_do_dia = pd.read_excel('G:\\Meu Drive\\Programacao\\futPythonTrader\\Jogos do dia\\'+str(dia)+'_Jogos_do_Dia_FlashScore.xlsx')
#jogos_do_dia = pd.read_excel('G:\\Meu Drive\\Programacao\\futPythonTrader\\Jogos do dia\\2023-05-21_Jogos_do_Dia_FlashScore.xlsx')
#jogos_do_dia = jogos_do_dia[['League','Round','Date','Time','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']] 
jogos_do_dia = jogos_do_dia[['League','Date','Time','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']] 
jogos_do_dia.dropna(inplace=True)
jogos_do_dia.reset_index(inplace=True, drop=True)
jogos_do_dia.index = jogos_do_dia.index.set_names(['Nº'])
Jogos_do_Dia = jogos_do_dia.rename(index=lambda x: x + 1)
#Jogos_do_Dia

# %%
lista=[]

for a,b,c,d,e,f,g,h,i,j,k,l in zip(Jogos_do_Dia.League,Jogos_do_Dia.Date,Jogos_do_Dia.Time,Jogos_do_Dia.Home,Jogos_do_Dia.Away,
                                   Jogos_do_Dia.FT_Odd_H,Jogos_do_Dia.FT_Odd_D,Jogos_do_Dia.FT_Odd_A,Jogos_do_Dia.FT_Odd_Over25,Jogos_do_Dia.FT_Odd_Under25,
                                   Jogos_do_Dia.FT_Odd_BTTS_Yes,Jogos_do_Dia.FT_Odd_BTTS_No):
        League = a
        Date = b
        Time = c
        home = d
        away = e
        FT_Odds_H = f
        FT_Odds_D = g
        FT_Odds_A = h
        FT_Odds_Over25 = i
        FT_Odds_Under25 = j
        FT_Odds_BTTS_Yes = k
        FT_Odds_BTTS_No = l
  
        df1 = base_H[base_H.Home == home].tail(1)

        df2 = base_A[base_A.Away == away].tail(1)

        jogo = {}

        jogo["League"] = League 
        jogo["Date"] = Date
        jogo["Time"] = Time
        jogo["Home"] = home
        jogo["Away"] = away
        jogo["FT_Odds_H"] = FT_Odds_H
        jogo["FT_Odds_D"] = FT_Odds_D
        jogo["FT_Odds_A"] = FT_Odds_A
        jogo["FT_Odds_Over25"] = FT_Odds_Over25
        jogo["FT_Odds_Under25"] = FT_Odds_Under25
        jogo["FT_Odds_BTTS_Yes"] = FT_Odds_BTTS_Yes
        jogo["FT_Odds_BTTS_No"] = FT_Odds_BTTS_No

        
        try:


            base_H = base[['Home', 'Porc_Over25FT_Home', 'Media_Gols_Sofridos_Home','CV_Gols_Feitos_Home']]

            base_A = base[['Away', 'Porc_BTTS_Away', 'CV_Gols_Sofridos_Away','CV_Gols_Feitos_Away']]        
            
            
            
            jogo['Porc_Over25FT_Home'] = df1[df1.Home == home]['Porc_Over25FT_Home'].iloc[0]
            jogo['Media_Gols_Sofridos_Home'] = df1[df1.Home == home]['Media_Gols_Sofridos_Home'].iloc[0]
            jogo['CV_Gols_Feitos_Home'] = df1[df1.Home == home]['CV_Gols_Feitos_Home'].iloc[0]


            jogo['Porc_BTTS_Away'] = df2[df2.Away == away]['Porc_BTTS_Away'].iloc[0]
            jogo['CV_Gols_Sofridos_Away'] = df2[df2.Away == away]['CV_Gols_Sofridos_Away'].iloc[0]
            jogo['CV_Gols_Feitos_Away'] = df2[df2.Away == away]['CV_Gols_Feitos_Away'].iloc[0]
           
            
        except:
            pass
        
        lista.append(jogo)


df = pd.DataFrame(lista)
#df.reset_index(inplace=True, drop=True)
df.index = df.index.set_names(['Nº'])
df = df.rename(index=lambda x: x + 1)

# CV das Odds do Match Odds
df['CV_HDA'] = df[['FT_Odds_H','FT_Odds_D','FT_Odds_A']].std(ddof=0, axis=1) / df[['FT_Odds_H','FT_Odds_D','FT_Odds_A']].mean(axis=1)
#df

# %%
flt = (
((df.FT_Odds_Over25 >= 1.8)) & ((df.FT_Odds_Over25 <= 3))
& ((df.FT_Odds_H >= 1)) & ((df.FT_Odds_H <= 4))
& ((df.Porc_Over25FT_Home >= 50))
& ((df.Porc_BTTS_Away >= 50))
& ((df.Media_Gols_Sofridos_Home >= 0.5)) & ((df.Media_Gols_Sofridos_Home <= 3))
& ((df.CV_Gols_Sofridos_Away >= 0.3)) & ((df.CV_Gols_Sofridos_Away <= 0.8))
& ((df.CV_Gols_Feitos_Away >= 0.5)) & ((df.CV_Gols_Feitos_Away <= 1.6))
& ((df.CV_Gols_Feitos_Home <= 1.6))
)

full25 = df[flt]
full25 = full25[['Date','Time','League','Home','Away','FT_Odds_H','FT_Odds_D','FT_Odds_A']]
full25 = drop_reset_index(full25)



from datetime import date, datetime, timedelta
data = datetime.today() + timedelta(1)
amanha = data.strftime('%Y-%m-%d')
#BTTS_Sim.to_excel(f'Entradas BTTS_Sim\\{amanha}_entrada_BTTS_Sim_.xlsx', index=None)
#BTTS_Sim

# %% [markdown]
# # Entradas

# %%
full25['Método'] = 'full25'
try:
    # Ler a planilha existente (se existir)
    dados_existentes = pd.read_excel(f'ApostasGeradas\\{amanha}_entradas.xlsx')
    
    # Concatenar DataFrame aos dados existentes
    dados_concatenados = pd.concat([dados_existentes, full25], ignore_index=True)
    # Salvar os dados concatenados na planilha existente
    
    dados_concatenados.to_excel(f'ApostasGeradas\\{amanha}_entradas.xlsx', index=False)
except FileNotFoundError:
    # Se o arquivo não existir, criar um novo com o DataFrame
    full25.to_excel(f'ApostasGeradas\\{amanha}_entradas.xlsx', index=False)
full25


