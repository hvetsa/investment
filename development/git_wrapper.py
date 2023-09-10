import os
import shutil

import git


def clone_git_repo(url, dir):

    repo = None
    try:
        if os.path.exists(dir + '_old'):
            print(f"_Old director exists, removing {dir + '_old'}.")
            shutil.rmtree(dir + '_old')

        if os.path.exists(dir):
            print(f"{dir} directory exists, Renaming to {dir + '_old'}.")
            os.rename(dir, dir + '_old')

        repo = git.Repo.clone_from(url, dir)
    except Exception as e:
        print(e)
        return repo

    return repo


if __name__ == '__main__':
    print(f'Starting the program {__file__} in standalone mode.')
    passwd = os.environ.get('GITHUB_TOKEN_HVETSA')
    user = os.environ.get('GITHUB_USER_HVETSA')
    rv = clone_git_repo(
        f'https://{user}:{passwd}@github.com/hvetsa/investment_config',
        '/tmp/x',
    )
    # if rv is None, clone failed.
    print(rv)
