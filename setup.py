from sys import version
from setuptools import _install_setup_requires, setup

ls=open("desc.txt","r")
setup(name='TOPSIS-parteekpal-101803190',version='0.3',packages=['topsis'],install_requires=['pandas','numpy'],long_description=ls.read())