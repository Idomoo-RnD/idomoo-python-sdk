# coding: utf-8

"""
    Idomoo API

    OpenAPI spec version: 2.0
    Contact: dev.support@idomoo.com
"""

from setuptools import setup, find_packages

NAME = "idomoo-python-sdk"
VERSION = "0.0.1-beta"

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Idomoo API",
    author_email="dev.support@idomoo.com",
    url="",
    keywords=["Idomoo API", "Idomoo", "SDK"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=""
)
