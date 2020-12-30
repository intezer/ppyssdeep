import os

import setuptools


def parse_requirements(requirement_list):
    for requirement in requirement_list:
        if not requirement.startswith('-r'):
            yield requirement
        else:
            file_to_read = requirement.lstrip('-r ')
            with open(os.path.join('requirements', file_to_read)) as req_file:
                for in_requirement in parse_requirements(req_file.readlines()):
                    yield in_requirement


def get_requirements():
    with open(os.path.join('requirements', 'all.txt'), 'r') as req_file:
        return list(parse_requirements(req_file.readlines()))


setuptools.setup(name='ppyssdeep',
                 version='0.0.2',
                 description='Pure python ssdeep hash.',
                 url='https://github.com/intezer/ppyssdeep',
                 packages=['ppyssdeep'],
                 install_requires=get_requirements(),
                 include_package_data=True)
