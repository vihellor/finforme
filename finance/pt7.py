import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

listaIPC = ['BMV:ALFAA',
            'BMV:ALPEKA',
            'BMV:ALSEA',
            'BMV:AMXL',
            'BMV:AC',
            'BMV:ASURB',
            'BMV:GFREGIOO',
            'BMV:BIMBOA',
            'BMV:BOLSAA',
            'BMV:CEMEXCPO',
            'BMV:KOFL',
            'BMV:LIVEPOLC-1',
            'BMV:ELEKTRA',
            'BMV:GFNORTEO',
            'BMV:FEMSAUBD',
            'BMV:LABB',
            'BMV:GENTERA',
            'BMV:GMEXICOB',
            'BMV:GRUMAB',
            'BMV:GAPB',
            'BMV:GCARSOA1',
            'BMV:GFINBURO',
            'BMV:SANMEXB',
            'BMV:LALAB',
            'BMV:TLEVISACPO',
            'BMV:IENOVA',
            'BMV:KIMBERA',
            'BMV:MEXCHEM',
            'BMV:NEMAKA',
            'BMV:OHLMEX',
            'BMV:OMAB',
            'BMV:PE&OLES',
            'BMV:PINFRA',
            'BMV:VOLARA',
            'BMV:WALMEX']

def save_ipc_tickers():
    tickers = []
    for row in listaIPC:
        ticker = row
        tickers.append(ticker)
        
    with open("ipctickers.pickle","wb") as f:
        pickle.dump(tickers,f)

    print(tickers)
    return tickers


def get_data_from_google(reload_sp500=False):
    
    if reload_sp500:
        tickers = save_ipc_tickers()
    else:
        with open("sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)
    
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2016, 12, 31)
    
    for ticker in tickers:
        # just in case your connection breaks, we'd like to save our progress!
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, "google", start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


def compile_data():
    with open("ipctickers.pickle","rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()
    
    for count,ticker in enumerate(tickers):
        df = pd.read_csv('stockipc_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns={'Close': ticker}, inplace=True)
        df.drop(['Open','High','Low','Volume'],1,inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print(count)
    print(main_df.tail())
    main_df.to_csv('sp500_joined_closes.csv')


compile_data()
