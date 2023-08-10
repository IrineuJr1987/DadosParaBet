# %%
import numpy as np
import pandas as pd
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

# %% [markdown]
# Conf do Chrome Driver

# %%
import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--no-sandbox")
#options.headless = True
#chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
wd_Chrome = webdriver.Chrome("/usr/bin/chromedriver", ChromeDriverManager().install(),options=chrome_options,)


# %%
# Com o WebDrive a gente consegue a pedir a página (URL)
wd_Chrome.get("https://www.flashscore.com.br/")
time.sleep(2)
# Fechando Botão de Cookies
try:
    button_cookies = wd_Chrome.find_element(By.CSS_SELECTOR,'button#onetrust-accept-btn-handler')
    button_cookies.click()
except:
    pass

time.sleep(3)

# %%
from datetime import date, datetime, timedelta
data = datetime.today() + timedelta(-1)
ontem = data.strftime('%Y-%m-%d')
print (ontem)

# Carregar o arquivo XLSX em um DataFrame do pandas



# %%
# placar1 = wd_Chrome.find_elements(By.CLASS_NAME,'event__score.event__score--home')[0].text
# placar2 = wd_Chrome.find_elements(By.CLASS_NAME,'event__score.event__score--away')[0].text

# placar1

# %%
try:
    #df = pd.read_excel(f'ApostasGeradas\\{ontem}_entradas.xlsx')
    df = pd.read_excel(f'ApostasGeradas\\{ontem}_entradas.xlsx')


    for index, row in df.iterrows():
        # Acessar os valores de cada coluna para a linha atual

        time1 = row['Home']

        wd_Chrome.find_element(By.XPATH,'//*[@id="search-window"]').click()
        time.sleep(3)
        wd_Chrome.find_element(By.XPATH,'//*[@id="search-window"]/div/div/div[2]/input').send_keys(time1)
        time.sleep(3)
        wd_Chrome.find_element(By.XPATH,'//*[@id="search-window"]/div/div/div[3]/div/a[1]/div[3]').click()
        wd_Chrome.find_element(By.XPATH,'//*[@id="li2"]').click()

        try:
            #verifica se foi pra penalti ou prorrogação
            div_pai = wd_Chrome.find_elements(By.CLASS_NAME,'event__time')[0]
            div_filha = div_pai.find_element(By.CLASS_NAME,'event__stage')

            placar1 = wd_Chrome.find_elements(By.CLASS_NAME,'event__part.event__part--home.event__part--2')[0].text
            placar2 = wd_Chrome.find_elements(By.CLASS_NAME,'event__part.event__part--away.event__part--2')[0].text


        except Exception:

            placar1 = wd_Chrome.find_elements(By.CLASS_NAME,'event__score.event__score--home')[0].text
            placar2 = wd_Chrome.find_elements(By.CLASS_NAME,'event__score.event__score--away')[0].text

        placar1=int(placar1)
        placar2=int(placar2)
        df.loc[index, 'PlacarHome'] = placar1
        df.loc[index, 'PlacarAway'] = placar2

        if df.loc[index, 'Método'] == "Back Draw":
            if placar1==placar2:
                df.loc[index, 'Green'] = "S"
                df.loc[index, 'GanhosPerdas'] = df.loc[index, 'Odd_Metodo'] - 1
            else:
                df.loc[index, 'Green'] = "N"
                df.loc[index, 'GanhosPerdas'] = -1
        
        if df.loc[index, 'Método'] == "BTTS_Sim":
            if placar1!=0 and placar2!=0:
                df.loc[index, 'Green'] = "S"
                df.loc[index, 'GanhosPerdas'] = df.loc[index, 'Odd_Metodo'] - 1
            else:
                df.loc[index, 'Green'] = "N"
                df.loc[index, 'GanhosPerdas'] = -1

        if df.loc[index, 'Método'] == "BTTS_Nao":
            if placar1== 0 or placar2==0:
                df.loc[index, 'Green'] = "S"
                df.loc[index, 'GanhosPerdas'] = df.loc[index, 'Odd_Metodo'] - 1
            else:
                df.loc[index, 'Green'] = "N"
                df.loc[index, 'GanhosPerdas'] = -1
                
        resultFinal = placar1 + placar2
        if df.loc[index, 'Método'] == "full25":
            if resultFinal > 2:
                df.loc[index, 'Green'] = "S"
                df.loc[index, 'GanhosPerdas'] = df.loc[index, 'Odd_Metodo'] - 1
            else:
                df.loc[index, 'Green'] = "N"
                df.loc[index, 'GanhosPerdas'] = -1
        

    #bttsnao bttsim full25
    # validar os metodos com a coluna green S ou N
    # calcular a porcentagem de perda e ganho
    df.to_excel(f'ApostasGeradas\\{ontem}_entradas.xlsx', index=False)
except FileNotFoundError:
    print ("Planilha não encontrada")



# %%



