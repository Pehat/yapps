#!/usr/bin/env python

from setuptools import setup, find_packages
import os
from yapps import __version__ as version

pkg_root = os.path.dirname(__file__)

# Error-handling here is to allow package to be built w/o README included
try:
    with open(os.path.join(pkg_root, 'README.txt')) as readme_file:
        readme = readme_file.read()
except IOError:
    readme = ''


setup(
    name = 'Yapps2',
    version = version,
    author = 'Amit J. Patel, Matthias Urlichs',
    author_email = 'amitp@cs.stanford.edu, smurf@debian.org',
    maintainer = 'Mike Kazantsev',
    maintainer_email = 'mk.fraggod@gmail.com',
    license = 'MIT',
    url = 'https://github.com/mk-fg/yapps',

    description = 'Yet Another Python Parser System',
    long_description = readme,

    packages = find_packages(),
    include_package_data = True,
    package_data = {'': ['README.txt']},
    exclude_package_data = {'': ['README.*']},

    entry_points = dict(console_scripts=[
        'yapps2 = yapps.cli_tool:main' ]),

    extras_require = {
        'dev': [
            'pytest==5.1.2',
            'pytest-cov==2.7.1',
            'python-coveralls==2.9.3',
            'tox==3.14.0'
        ]}
)
