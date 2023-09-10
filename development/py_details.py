import platform

import pkg_resources


def get_python_version():
    return platform.python_version()


def get_installed_packages():

    ip_objects = []
    ip_names = []

    installed_packages = pkg_resources.working_set
    for i in installed_packages:
        ip_objects.append(i)
        ip_names.append(i.key)

    return ip_objects, ip_names


def check_required_packages_installed(req_pkgs):
    missing_pkgs = []
    matched_pkgs = []
    ip_objects, ip_names = get_installed_packages()

    for pkg in req_pkgs:
        if pkg in ip_names:
            matched_pkgs.append(pkg)
        else:
            missing_pkgs.append(pkg)

    if missing_pkgs == []:
        return True, 'All required packages are matched.'
    else:
        return False, f'The following packages are missing: {missing_pkgs}'


if __name__ == '__main__':
    print(f'Starting the program {__file__} in standalone mode.')
    rv = get_python_version()
    print(f'Using python version {rv}')

    ip_objects, ip_names = get_installed_packages()
    print(f'Current installed modules: {ip_names}')

    ret_code, ret_message = check_required_packages_installed(['robin-stocks'])
    print(f'{ret_code} - {ret_message}')
