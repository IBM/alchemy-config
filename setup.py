#*****************************************************************#
# (C) Copyright IBM Corporation 2020.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
#*****************************************************************#

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'LICENSE')) as f:
    license = f.read()

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements.txt')) as f:
    requirements = f.readlines()

setup(
    name='aconfig',
    version='1.0.3',
    description='Configuration framework in Python for general configuration use.',
    long_description=long_description,
    url='https://github.ibm.com/watson-nlu/aconfig-py',
    author='Ethan Koch - IBM Watson',
    author_email='ethankoch@ibm.com',
    license=license,
    keywords='config',
    packages=['aconfig'],
    install_requires=requirements,
)
