# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Bade_python_example_project',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Bavo Denys',
    author_email='bavo.denys@tremec.com',
    url='https://bitbucket.org/controls-tremec/sandboxbade',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)