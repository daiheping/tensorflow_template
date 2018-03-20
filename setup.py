#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: huay
# Mail: imhuay@163.com
# Created Time:  2018-1-26 11:33:13
#############################################

from setuptools import setup, find_packages

setup(
    name="tensorflow_template",
    version="0.1",
    keywords=("huay", "tensorflow_template"),
    description="huay's tensorflow template",
    long_description="huay's tensorflow template",
    license="MIT Licence",

    url="https://github.com/imhuay/tensorflow_template",
    author="huay",
    author_email="imhuay@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['bunch'],  # ['tensorflow', 'numpy']  # too big
)
