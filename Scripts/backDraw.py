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
# # df1 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/ENGLAND%20-%20CHAMPIONSHIP.csv?raw=true")
# # df2 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/ENGLAND%20-%20PREMIER%20LEAGUE.csv?raw=true")
# # df3 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/FRANCE%20-%20LIGUE%201.csv?raw=true")
# # df4 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/FRANCE%20-%20LIGUE%202.csv?raw=true")
# # df5 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/GERMANY%20-%202.%20BUNDESLIGA.csv?raw=true")
# # df6 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/GERMANY%20-%20BUNDESLIGA.csv?raw=true")
# # df7 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/ITALY%20-%20SERIE%20A.csv?raw=true")
# # df8 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/ITALY%20-%20SERIE%20B.csv?raw=true")
# # df9 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/SPAIN%20-%20LALIGA.csv?raw=true")
# # df10 = pd.read_csv("https://github.com/futpythontrader/YouTube/blob/main/Base_de_Dados/FlashScore/SPAIN%20-%20LALIGA2.csv?raw=true")
# # df1 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E0.csv")#inglaterra 1
# # df2 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/E0.csv")#inglaterra 1
# # df3 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/E1.csv") #inglaterra 2
# # df4 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E1.csv") #inglaterra 2
# # df5 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/D1.csv")#alemanha1
# # df6 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/D1.csv")#alemanha1
# # df7 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/D2.csv")#alemanha2
# # df8 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/D2.csv")#alemanha2
# # df9 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/I1.csv") #italia A
# # df10 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/I1.csv") #italia A
# # df11 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/I2.csv") #italia B
# # df12 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/I2.csv") #italia B
# # df13 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/SP1.csv") #spain 1
# # df14 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/SP1.csv") #spain 1
# # df15 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/SP2.csv") #spain 2
# # df16 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/SP2.csv") #spain 2
# # df17 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/F1.csv") #franca 1
# # df18 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/F1.csv") #franca 1
# # df19 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/F2.csv") #franca 2
# # df20 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/F2.csv") #franca 2
# #df21 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/N1.csv") #holanda 1
# #df22 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/N1.csv") #holanda 1

# df1 = pd.read_excel("G:\\Meu Drive\\Programacao\\futPythonTrader\\BasesDeDados\\x_FutPythonTrader_Base_de_Dados_Temporada_2122_x.xlsx")
# df2 = pd.read_excel("https://github.com/futpythontrader/YouTube/raw/main/x_FutPythonTrader_Base_de_Dados_Temporada_Atual_x.xlsx")


# df = pd.concat([df1,df2])
# df.reset_index(inplace=True, drop=True)
# df.index = df.index.set_names(['Nº'])
# df = df.rename(index=lambda x: x + 1)

# #df = df[['Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','B365H','B365D','B365A','B365>2.5', 'B365<2.5']]
# df = df[['Date','League','Home','Away','Season','FT_Goals_H','FT_Goals_A','FT_Odds_H','FT_Odds_D','FT_Odds_A','FT_Odds_Over25','FT_Odds_Under25','Odds_BTTS_Yes','Odds_BTTS_No']]

# #df = df.rename(columns={'Div': 'League', 'Date': 'Date', 'HomeTeam': 'Home', 'AwayTeam': 'Away', 'FTHG': 'FT_Goals_H', 'FTAG': 'FT_Goals_A', 'B365H': 'FT_Odd_H', 'B365D': 'FT_Odd_D', 'B365A': 'FT_Odd_A', 'B365>2.5': 'FT_Odd_Over25', 'B365<2.5': 'FT_Odd_Under25'})

# #df = df[['League', 'Date','Time','Home','Away','Season','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']]
# #gols full time home
# #gols full time away
# #full time odd home
# #full time odd away
# #full time odd draw
# #full time odd over 2.5
# #full time odd under 2.5
# #full time btts yes
# #full time btts no

# #df = drop_reset_index(df)

# df

# %%
# flt = ((df.FT_Odds_H != 0) & (df.FT_Odds_D != 0) & (df.FT_Odds_A != 0))
# df = df[flt]

# df["Total_Goals"] = df["FT_Goals_H"] + df["FT_Goals_A"]

# df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'FT_Result'] = "H"
# df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'FT_Result'] = "D"
# df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'FT_Result'] = "A"

# # Profit
# green = df.FT_Odds_D - 1
# red = -1

# df.loc[df['FT_Result'] == "D", 'Profit'] = green
# df.loc[df['FT_Result'] != "D", 'Profit'] = red

# # Probabilidades
# df['p_H'] = 1 / df.FT_Odds_H
# df['p_D'] = 1 / df.FT_Odds_D
# df['p_A'] = 1 / df.FT_Odds_A

# # CV das Odds do Match Odds
# df['CV_HDA'] = df[['p_H','p_D','p_A']].std(ddof=0, axis=1) / df[['p_H','p_D','p_A']].mean(axis=1)

# # Pontos
# df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'Ptos_H'] = 3
# df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'Ptos_H'] = 1
# df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'Ptos_H'] = 0

# df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'Ptos_A'] = 3
# df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'Ptos_A'] = 1
# df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'Ptos_A'] = 0

# df["Ptos_H"] = df["Ptos_H"].astype('int64')
# df["Ptos_A"] = df["Ptos_A"].astype('int64')

# df['Media_Ptos_H'] = df.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
# df['Media_Ptos_A'] = df.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

# df['Media_Ptos_H'] = df.groupby('Home')['Media_Ptos_H'].shift(1)
# df['Media_Ptos_A'] = df.groupby('Away')['Media_Ptos_A'].shift(1)

# df['DesvPad_Ptos_H'] = df.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
# df['DesvPad_Ptos_A'] = df.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

# df['DesvPad_Ptos_H'] = df.groupby('Home')['DesvPad_Ptos_H'].shift(1)
# df['DesvPad_Ptos_A'] = df.groupby('Away')['DesvPad_Ptos_A'].shift(1)

# df['CV_Ptos_H'] = df['DesvPad_Ptos_H'] / df['Media_Ptos_H']
# df['CV_Ptos_A'] = df['DesvPad_Ptos_A'] / df['Media_Ptos_A']

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

# df = df.drop(['Ptos_H','Ptos_A','VG_H', 'VG_A', 'CG_H', 'CG_A'], axis=1)
# df.to_excel(f'teste_Back_Draw_.xlsx', index=None)
# df

# %% [markdown]
# # Filtros do Método

# %%
# flt = (
# ((df.CV_HDA >= 0.2) & (df.CV_HDA <= 0.3))
# & ((df.FT_Odds_H > 1.5) & (df.FT_Odds_H < 3.5))
# & ((df.FT_Odds_D > 3)) & ((df.FT_Odds_D < 4.02))
# & ((df.FT_Odds_A > 1.52)) & ((df.FT_Odds_A < 4))
# & ((df.FT_Odds_Under25 >= 1.01) & (df.FT_Odds_Under25 <= 3))
# & ((df.Media_VG_A >= 0.153)) & ((df.Media_VG_A <= 1.85))
# & ((df.CV_CG_A <= 0.8))
# & ((df.CV_CG_H > 0.2)) & ((df.CV_CG_H < 0.6))
# )


# df = df[df['League'].isin(["Austria Bundesliga",
# "Bolivia LFPB",
# "Brazil Serie B",
# "Brazil Serie D",
# "Canada Canadian Premier League",
# "China Chinese Super League",
# "Croatia Prva HNL",
# "Czech Republic First League",
# "Denmark Superliga",
# "Germany 2. Bundesliga",
# "Italy Serie A",
# "Italy Serie B",
# "Mexico Liga MX",
# "Poland Ekstraklasa",
# "Romania Liga I",
# "Scotland Premiership",
# "Spain La Liga",
# "Switzerland Super League",
# "Uruguay Primera División",
# "USA MLS",
# "Venezuela Primera División",
# "Wales Welsh Premier League"]) == True]
# df0 = df[flt]
# grafico(df0,'Back Empate')

# %% [markdown]
# # Unindo a Base de Dados com os Jogos do Dia

# %%
# df0['League'].unique()

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
# base['League'].unique()

# %%
base = base[base['League'].isin(["Austria Bundesliga",
"Bolivia LFPB",
"Brazil Serie B",
"Brazil Serie D",
"Canada Canadian Premier League",
"China Chinese Super League",
"Croatia Prva HNL",
"Czech Republic First League",
"Denmark Superliga",
"Germany 2. Bundesliga",
"Italy Serie A",
"Italy Serie B",
"Mexico Liga MX",
"Poland Ekstraklasa",
"Romania Liga I",
"Scotland Premiership",
"Spain La Liga",
"Switzerland Super League",
"Uruguay Primera División",
"USA MLS",
"Venezuela Primera División",
"Wales Welsh Premier League"]) == True]

# %%
flt = ((base.FT_Odds_H != 0) & (base.FT_Odds_D != 0) & (base.FT_Odds_A != 0))
base = base[flt]

base["Total_Goals"] = base["FT_Goals_H"] + base["FT_Goals_A"]

base.loc[base['FT_Goals_H'] > base['FT_Goals_A'], 'FT_Result'] = "H"
base.loc[base['FT_Goals_H'] == base['FT_Goals_A'], 'FT_Result'] = "D"
base.loc[base['FT_Goals_H'] < base['FT_Goals_A'], 'FT_Result'] = "A"

# Profit
green = base.FT_Odds_D - 1
red = -1

base.loc[base['FT_Result'] == "D", 'Profit'] = green
base.loc[base['FT_Result'] != "D", 'Profit'] = red

# Probabilidades
base['p_H'] = 1 / base.FT_Odds_H
base['p_D'] = 1 / base.FT_Odds_D
base['p_A'] = 1 / base.FT_Odds_A

# CV das Odds do Match Odds
base['CV_HDA'] = base[['p_H','p_D','p_A']].std(ddof=0, axis=1) / base[['p_H','p_D','p_A']].mean(axis=1)

# Pontos
base.loc[base['FT_Goals_H'] > base['FT_Goals_A'], 'Ptos_H'] = 3
base.loc[base['FT_Goals_H'] == base['FT_Goals_A'], 'Ptos_H'] = 1
base.loc[base['FT_Goals_H'] < base['FT_Goals_A'], 'Ptos_H'] = 0

base.loc[base['FT_Goals_H'] < base['FT_Goals_A'], 'Ptos_A'] = 3
base.loc[base['FT_Goals_H'] == base['FT_Goals_A'], 'Ptos_A'] = 1
base.loc[base['FT_Goals_H'] > base['FT_Goals_A'], 'Ptos_A'] = 0

base["Ptos_H"] = base["Ptos_H"].astype('int64')
base["Ptos_A"] = base["Ptos_A"].astype('int64')

base['Media_Ptos_H'] = base.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
base['Media_Ptos_A'] = base.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

base['Media_Ptos_H'] = base.groupby('Home')['Media_Ptos_H'].shift(1)
base['Media_Ptos_A'] = base.groupby('Away')['Media_Ptos_A'].shift(1)

base['DesvPad_Ptos_H'] = base.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
base['DesvPad_Ptos_A'] = base.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

base['DesvPad_Ptos_H'] = base.groupby('Home')['DesvPad_Ptos_H'].shift(1)
base['DesvPad_Ptos_A'] = base.groupby('Away')['DesvPad_Ptos_A'].shift(1)

base['CV_Ptos_H'] = base['DesvPad_Ptos_H'] / base['Media_Ptos_H']
base['CV_Ptos_A'] = base['DesvPad_Ptos_A'] / base['Media_Ptos_A']

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

base = base.drop(['Ptos_H','Ptos_A','VG_H', 'VG_A', 'CG_H', 'CG_A'], axis=1)

# %%
base = drop_reset_index(base)
# base

# %%
# base.columns.to_list()

# %%
base_H = base[['Home', 'Media_Ptos_H', 'DesvPad_Ptos_H', 'CV_Ptos_H', 'Media_VG_H', 'DesvPad_VG_H', 'CV_VG_H', 'Media_CG_H', 'DesvPad_CG_H', 'CV_CG_H']]

base_H = base[['Home', 'CV_HDA', 'Media_VG_H', 'CV_CG_H']]

base_A = base[['Away', 'CV_HDA', 'Media_VG_A', 'CV_CG_A']]

#base_H.to_excel('baseh.xlsx', index=None)

# %%
from datetime import date, datetime, timedelta
dia = date.today() - timedelta(-1)
print(dia)

# %%
#jogos_do_dia = pd.read_csv('https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_FlashScore/'+str(dia)+'_Jogos_do_Dia_FlashScore.csv?raw=true')
jogos_do_dia = pd.read_excel('G:\\Meu Drive\\Programacao\\futPythonTrader\\Jogos do dia\\'+str(dia)+'_Jogos_do_Dia_FlashScore.xlsx')
#jogos_do_dia = pd.read_excel('G:\\Meu Drive\\Programacao\\futPythonTrader\\Jogos do dia\\2023-04-22_Jogos_do_Dia_FlashScore.xlsx')
#jogos_do_dia = jogos_do_dia[['League','Round','Date','Time','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']] 
jogos_do_dia = jogos_do_dia[['League','Date','Time','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No']] 
jogos_do_dia.dropna(inplace=True)
jogos_do_dia.reset_index(inplace=True, drop=True)
jogos_do_dia.index = jogos_do_dia.index.set_names(['Nº'])
Jogos_do_Dia = jogos_do_dia.rename(index=lambda x: x + 1)
# Jogos_do_Dia

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

            base_H = base[['Home', 'CV_HDA', 'Media_VG_H', 'CV_CG_H']]

            base_A = base[['Away', 'CV_HDA', 'Media_VG_A', 'CV_CG_A']]
        
            
            
            
            jogo['Media_VG_H'] = df1[df1.Home == home]['Media_VG_H'].iloc[0]
            jogo['CV_CG_H'] = df1[df1.Home == home]['CV_CG_H'].iloc[0]


            jogo['Media_VG_A'] = df2[df2.Away == away]['Media_VG_A'].iloc[0]
            jogo['CV_CG_A'] = df2[df2.Away == away]['CV_CG_A'].iloc[0]
            
        except:
            pass
        
        lista.append(jogo)


df = pd.DataFrame(lista)
#df.reset_index(inplace=True, drop=True)
df.index = df.index.set_names(['Nº'])
df = df.rename(index=lambda x: x + 1)

# CV das Odds do Match Odds
df['CV_HDA'] = df[['FT_Odds_H','FT_Odds_D','FT_Odds_A']].std(ddof=0, axis=1) / df[['FT_Odds_H','FT_Odds_D','FT_Odds_A']].mean(axis=1)
# df

# %%
flt = (
((df.CV_HDA >= 0.2) & (df.CV_HDA <= 0.3))
& ((df.FT_Odds_H > 1.5) & (df.FT_Odds_H < 3.5))
& ((df.FT_Odds_D > 3)) & ((df.FT_Odds_D < 4.02))
& ((df.FT_Odds_A > 1.52)) & ((df.FT_Odds_A < 4))
& ((df.FT_Odds_Under25 >= 1.01) & (df.FT_Odds_Under25 <= 3))
& ((df.Media_VG_A >= 0.153)) & ((df.Media_VG_A <= 1.85))
& ((df.CV_CG_A <= 0.8))
& ((df.CV_CG_H > 0.2)) & ((df.CV_CG_H < 0.6))
)

Back_Draw = df[flt]
Back_Draw = Back_Draw[['Date','Time','League','Home','Away','FT_Odds_H','FT_Odds_D','FT_Odds_A']]

Back_Draw = drop_reset_index(Back_Draw)



from datetime import date, datetime, timedelta
data = datetime.today() + timedelta(1)
amanha = data.strftime('%Y-%m-%d')
#Back_Draw.to_excel(f'Entradas Back_Draw\\{amanha}_entrada_Back_Draw_.xlsx', index=None)
#Back_Draw

# %% [markdown]
# # Entradas

# %%
Back_Draw['Método'] = 'Back Draw'
try:
    # Ler a planilha existente (se existir)
    dados_existentes = pd.read_excel(f'ApostasGeradas\\{amanha}_entradas.xlsx')
    
    # Concatenar DataFrame aos dados existentes
    dados_concatenados = pd.concat([dados_existentes, Back_Draw], ignore_index=True)
    # Salvar os dados concatenados na planilha existente
    
    dados_concatenados.to_excel(f'ApostasGeradas\\{amanha}_entradas.xlsx', index=False)
except FileNotFoundError:
    # Se o arquivo não existir, criar um novo com o DataFrame
    Back_Draw.to_excel(f'ApostasGeradas\\{amanha}_entradas.xlsx', index=False)
Back_Draw


