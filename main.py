# data packages | Note: using yfinance package to stream data from yahoo finance
import pandas as pd
import numpy as np
import yfinance as yf

# visualization packages
import plotly.graph_objects as go
import datetime as dt


# cleaning input
def check_stk(stk):
    tck = yf.Ticker(stk)
    try:
        info=tck.info
    except:
        return False
    else:
        print (info)
        return True

def check_prd_inl (data):
    if data.isDigit(): return True
    else: return False

def plot (tck, prd, inl):
    df = yf.download (tickers=tck, period=prd, interval=inl)
    fig = go.Figure()
    # making a basic candle stick chart (like the one we see on buy/sell trade platforms)
    fig.add_trace(go.Candlestick(x=df.index, 
                                 open=df['Open',tck],
                                 high=df['High',tck],
                                 low=df['Low',tck],
                                 close=df['Close',tck],
                                 name='market data'))
    # updating layout with title and axis labels
    fig.update_layout(title=str(tck) + ' Live Share Price:', yaxis_title='Stock Price (USD per shares)')

    # adding sliders for the x-axis to control the intervals
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label='15m', step='minute', stepmode='backward'),
                dict(count=45, label='45m', step='minute', stepmode='backward'),
                dict(count=1, label='HTD', step='hour', stepmode='todate'),
                dict(count=3, label='3h', step='hour', stepmode='backward'),
                dict(step='all')
            ])
        )
    )
    fig.show()



def main():
    # get input from users
    stk = input ("Enter stock listing name: ")
    prd = input ("Enter period of listing: ")
    inl = input ("Enter interval minutes for listing: ")
    
    plot(stk,prd,inl)

main()