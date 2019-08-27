#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)
cola = __import__('cola')
# version = cola.VERSION


setup(
    name='cola',
    version='0.1',
    description='A high-level distributed crawling framework',
    # long_description=long_description,
    author='peniridis',
    author_email='roocpeng@foxmail.com',
    license='Apache 2',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    # entry_points={
    #     'console_scripts': ['coca = cola.cmdline:execute']
    # },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Clustering'
    ],
    install_requires=[]
)
