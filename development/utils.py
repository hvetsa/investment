import os

import yaml


def get_config():

    config_file = os.path.dirname(__file__) + '/config.yaml'
    conf = None
    try:
        conf = yaml.safe_load(open(config_file).read())
        gu = os.environ.get(conf['gh_user_env'])
        gt = os.environ.get(conf['gh_token_env'])
        conf['git_url'] = conf['git_url'].replace('GITHUB_USER_HVETSA', gu)
        conf['git_url'] = conf['git_url'].replace('GITHUB_TOKEN_HVETSA', gt)

    except Exception as e:
        print(e)

    return conf


# end get_config()


if __name__ == '__main__':
    print(f'Starting the program {__file__} in standalone mode.')
    conf = get_config()
    print(conf)
