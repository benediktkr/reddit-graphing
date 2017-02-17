# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(
    name='reddit-graphing',
    version="0.1.0",
    author='Lehmann',
    author_email='benedikt@inventati.org',
    description='Looking at reddit',
    packages=find_packages(
        exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    entry_points={
        'console_scripts': [
            #'init_data = in2_auth.scripts:init_data',
        ]
    })
