"""Python bindings for Marvel Comics API
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
from marvelous import (__version__, __author__, __license__)

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='marvelous',
    version=__version__,

    description      = 'Python bindings for Marvel Comics API',
    long_description = long_description,
    url              = 'https://github.com/dcloud/marvelous',
    license          = __license__,

    author       = __author__,
    author_email = 'daniel+marvelous@danielcloud.org',

    platforms   = ['any'],
    classifiers = [
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['requests'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
