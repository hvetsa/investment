import git_wrapper as gw
import robinhood_wrapper as rw
import utils
import yfinance_wrapper as yw


def main():
    conf = pre_flight()
    if 1 == 2:
        print(conf)

    return True


# end main()


def pre_flight():
    # obtain configuration to start the program
    conf = utils.get_config()

    # clone investment config repo
    conf['cloned_git_repo'] = gw.clone_git_repo(conf['git_url'], conf['config_git_dir'])

    # Robinhood ping
    conf['robinhood_logged_in'] = rw.robin_logged_in()

    # Yahoo ping
    conf['yfinance_test'] = yw.yfinance_sample_test()

    return conf


# end pre_flight()


if __name__ == '__main__':
    print(f'Starting the program {__file__} in standalone mode.')
    rv = main()
    print(rv)
