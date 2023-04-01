# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Python_example_project',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Bavo Denys',
    author_email='',
    url='https://github.com/bavodenys/python_project_example',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
