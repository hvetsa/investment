#!/usr/bin/env python3
import yfinance as yf


def insights():
    data_dir = '/Documents/investment'
    tickers = ['MSFT']
    msft = yf.Ticker('MSFT')
    history = msft.history(period='3650d')
    print(history)
    print(data_dir, tickers)


if __name__ == '__main__':
    print('Hello!')
    rv = insights()
