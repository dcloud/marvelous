"""Python bindings for Marvel Comics API
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

import marvelous

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='marvelous',
    version=marvelous.__version__,

    description='Python bindings for Marvel Comics API',
    long_description=long_description,

    url='https://github.com/dcloud/marvelous',

    author=marvelous.__author__,
    author_email='daniel+marvelous@danielcloud.org',

    license=marvelous.__license__,

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Topic :: Internet :: WWW/HTTP',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='marvel comics api',

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
