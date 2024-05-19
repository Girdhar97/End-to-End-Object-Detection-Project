# Setup.py file looks for all constructive files in all the folders and it will install that folder as my local package

from setuptools import find_packages, setup

setup(
    name = 'signLanguages',
    version= '0.0.0',
    author= 'iNeuron',
    author_email= 'boktiar@ineuron.ai',
    packages= find_packages(),
    install_requires = []

)