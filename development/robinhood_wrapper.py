import robin_stocks


def robin_logged_in():

    # logged_in = robin_stocks.robinhood.account.LOGGED_IN
    up = None
    logged_in = None
    try:
        up = robin_stocks.robinhood.account.load_user_profile()
        if up:
            logged_in = True

    except Exception as e:
        print(e)
        logged_in = False

    return logged_in


# end main()


def robinhood_login(ru, rp):

    login = None
    result = None
    try:
        login = robin_stocks.robinhood.login(ru, rp)
        if login:
            result = True

    except Exception as e:
        print(e)
        result = False

    return result, login


if __name__ == '__main__':
    print(f'Starting the program {__file__} in standalone mode.')
    print(robin_logged_in())
