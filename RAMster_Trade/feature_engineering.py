import pandas as pd
from sklearn import preprocessing
from functions import gain, loss
import requests


# Relative Strength Index - Indicador de sobrecompra e sobrevenda
# Considerando 14 periodos
def rsi(df):    
    # Create a list, fill first 14 values with 'None'
    rsi_list = [None for i in range(14)]    
    df = df.change
    
    # Calculating first RSI
    avg_gain = sum([i for i in df[1:15] if i > 0])/14
    avg_loss = sum([abs(i) for i in df[1:15] if i < 0])/14
    rs = avg_gain / avg_loss
    rsi = 100 - ( 100 / ( 1 + rs ))
    rsi_list.append(rsi)
    
    # Calculating following RSI's
    for i in range(15, len(df)):
        avg_gain = (avg_gain * 13 + gain(df[i]))/14
        avg_loss = (avg_loss * 13 + loss(df[i]))/14
        rs = avg_gain / avg_loss
        rsi = 100 - ( 100 / ( 1 + rs ))
        rsi_list.append(rsi)
    
    return rsi_list   
 
# Moving Average Convergence/Divergence        
# Considerando 9 periodos
def macd(df):
    exp1 = df.close.ewm(span=12, adjust=False).mean()
    exp2 = df.close.ewm(span=26, adjust=False).mean()
    macd = exp1-exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal
 
# Bollinger Bands    
# Considerando média móvel de 21 periodos e desvio padrão de 2
def bollinger_bands(df, window=21):
    rolling_mean = df.close.rolling(window).mean()
    rolling_std = df.close.rolling(window).std()
    upper_band = rolling_mean + (rolling_std*2)
    lower_band = rolling_mean - (rolling_std*2)
    return upper_band, lower_band
 
    
def momentum(data, n_days):
    m = [None for i in range(n_days)]    
    for i in range(len(data) - n_days):
        end = i + n_days
        m.append(data[i] - n_days)
    return m

####################################################
### Analise de sentimento site: nasdaq.com
####################################################    
def get_headlines(page):
    html = requests.get(page).text
    soup = BeautifulSoup(html)    
    headlines = soup.find_all("a", { "target" : "_self" })
    headlines.pop(0)
    dates = soup.findAll('small')
    dates.pop(0)
    return [i.text.strip() for i in headlines], [i.text.strip().split()[0] for i in dates]