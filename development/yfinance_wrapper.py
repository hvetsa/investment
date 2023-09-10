import yfinance as yf


def yfinance_sample_test():

    msft = None
    try:
        msft = yf.Ticker('MSFT')
        if msft:
            return True
    except Exception as e:
        print(e)
        return False


# end yfinance_sample_test()


if __name__ == '__main__':
    print(f'Starting the program {__file__} in standalone mode.')
    print(yfinance_sample_test())
