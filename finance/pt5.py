import bs4 as bs
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

save_ipc_tickers()
