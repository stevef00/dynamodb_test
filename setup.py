#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

PROJECT = 'bkmk'

# change docs/sphinx/conf.py too!
VERSION = '0.1'

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name = PROJECT,
    version = VERSION,

    description = 'a simple bookmark manager',
    long_description = long_description,

    author = 'Steve Feehan',
    author_email = 'stevef00@pobox.com',

    url = 'https://github.com/stevef00/bkmk',
    download_url = 'https://github.com/stevef00/bkmk/tarball/master',

    # https://pypi.org/classifiers/
    classifiers = [
        'Private :: Do Not Upload',
        'Development Status :: 1 - Planning',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],

    scripts = [],

    provides = [],
    install_requires = [ 'cliff', 'boto3', 'ulid-py' ],

    namespace_packages = [],
    packages = find_packages(),
    include_package_data = True,

    entry_points = {
        'console_scripts': [
            'bkmk = bkmk.main:main'
        ],
        'bkmk': [
            'add = bkmk.add:Add',
            'list = bkmk.list:List',
            'rm = bkmk.rm:Rm',
        ]
    },

    zip_safe = False,
)
