# %%
import pandas as pd
import numpy as np

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

import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.headless = True

from selenium.webdriver.chrome.service import Service
wd_Chrome = webdriver.Chrome("/usr/bin/chromedriver", options=options)

# Com o WebDrive a gente consegue a pedir a página (URL)
wd_Chrome.get("https://www.flashscore.com/")

# Fechando Botão de Cookies
try:
    button_cookies = wd_Chrome.find_element(By.CSS_SELECTOR,'button#onetrust-accept-btn-handler')
    button_cookies.click()
except:
    pass

# Selecionando o Dia de Amanhã
wd_Chrome.find_element(By.CSS_SELECTOR,'button.calendar__navigation--tomorrow').click()
time.sleep(3)

# Pegando o ID dos Jogos
id_jogos = []
jogos = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.event__match--scheduled')

for i in jogos:
    id_jogos.append(i.get_attribute("id"))

# Exemplo de ID de um jogo: 'g_1_Gb7buXVt'    
id_jogos = [i[4:] for i in id_jogos]

jogo = {'Date':[],'Time':[],'Country':[],'League':[],'Home':[],'Away':[],'Odd_H':[],'Odd_D':[],'Odd_A':[],'Odd_Over15':[],'Odd_Under15':[],'Odd_Over25':[],'Odd_Under25':[],'Odd_BTTS_Yes':[],'Odd_BTTS_No':[]}

# %%
# Pegando as Informacoes Básicas do Jogo
for link in tqdm(id_jogos, total=len(id_jogos)):
    wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/match-summary')
    
    try:
        Date = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__startTime').text.split(' ')[0]
        Time = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__startTime').text.split(' ')[1]
        Country = wd_Chrome.find_element(By.CSS_SELECTOR,'span.tournamentHeader__country').text.split(':')[0]
        League = wd_Chrome.find_element(By.CSS_SELECTOR,'span.tournamentHeader__country')
        League = League.find_element(By.CSS_SELECTOR,'a').text
        Home = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__home')
        Home = Home.find_element(By.CSS_SELECTOR,'div.participant__participantName').text
        Away = wd_Chrome.find_element(By.CSS_SELECTOR,'div.duelParticipant__away')
        Away = Away.find_element(By.CSS_SELECTOR,'div.participant__participantName').text
    except:
        pass

# Match Odds
    try:
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/1x2-odds/full-time')
        time.sleep(2)
        
        linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
        
        for linha in linhas:
                Odd_H = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                Odd_D = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text) 
                Odd_A = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[2].text)
    except:
        pass

# Over e Under 2.5
    try:
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/over-under/full-time')
        time.sleep(2)
        
        linhas_over_under = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table.oddsCell__odds')
        for i in linhas_over_under:
            linhas = i.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
            for linha in linhas:
                try:
                    qtd_gols = linha.find_element(By.CSS_SELECTOR,'span.oddsCell__noOddsCell').text.replace('.','')
                    if qtd_gols == '05':
                        Odd_Over05 = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                        Odd_Under05 = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                    if qtd_gols == '15':
                        Odd_Over15 = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                        Odd_Under15 = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                        #print(Odd_Under15)
                    if qtd_gols == '25':
                        Odd_Over25 = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                        Odd_Under25 = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
                except:
                    pass
    except:
        pass

# Ambas Marcam (BTTS)
    try:
        wd_Chrome.get(f'https://www.flashscore.com/match/{link}/#/odds-comparison/both-teams-to-score/full-time')
        time.sleep(2)
    
        linhas = wd_Chrome.find_elements(By.CSS_SELECTOR,'div.ui-table__row')
        
        for linha in linhas:
                BTTS_Yes = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[0].text)
                BTTS_No = float(linha.find_elements(By.CSS_SELECTOR,'a.oddsCell__odd')[1].text)
    except:
        pass    
    
    try:
        print(Date,Time,Country,League,Home,Away,Odd_H,Odd_D,Odd_A,Odd_Over15,Odd_Under15,Odd_Over25,Odd_Under25,BTTS_Yes,BTTS_No) 

        jogo['Date'].append(Date)
        jogo['Time'].append(Time)
        jogo['Country'].append(Country)
        jogo['League'].append(League)
        jogo['Home'].append(Home)
        jogo['Away'].append(Away)
        jogo['Odd_H'].append(Odd_H)
        jogo['Odd_D'].append(Odd_D)
        jogo['Odd_A'].append(Odd_A)
        jogo['Odd_Over15'].append(Odd_Over15)
        jogo['Odd_Under15'].append(Odd_Under15)
        jogo['Odd_Over25'].append(Odd_Over25)
        jogo['Odd_Under25'].append(Odd_Under25)
        jogo['Odd_BTTS_Yes'].append(BTTS_Yes)
        jogo['Odd_BTTS_No'].append(BTTS_No)

    except:
        pass

# %% [markdown]
# ## Gerando DataFrame com os Jogos do Dia

# %%
df = pd.DataFrame(jogo)
df = drop_reset_index(df)
df

# %%
df = df.rename(columns={'Odd_H': 'FT_Odd_H',
                        'Odd_D': 'FT_Odd_D',
                        'Odd_A': 'FT_Odd_A',
                        'Odd_Over15': 'FT_Odd_Over15',
                        'Odd_Under15': 'FT_Odd_Under15',
                        'Odd_Over25': 'FT_Odd_Over25',
                        'Odd_Under25': 'FT_Odd_Under25',
                        'Odd_BTTS_Yes': 'FT_Odd_BTTS_Yes',
                        'Odd_BTTS_No': 'FT_Odd_BTTS_No',
                        })

# %%
# Gerando os dados para excel
from datetime import date, datetime, timedelta
data = datetime.today() + timedelta(1)
amanha = data.strftime('%Y-%m-%d')
nome = 'Jogos_do_Dia_FlashScore.xlsx'

df.to_excel(f'G:\\Meu Drive\\Programacao\\futPythonTrader\\Jogos do dia\\{amanha}_{nome}', index = False)


