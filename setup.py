# :coding: utf-8
# :copyright: Copyright (c) 2015 ftrack

import os
import sys
import re
import shutil

from setuptools import Command
import subprocess

from setuptools import find_packages, setup

# Configuration.
setup(
    name='ftrack-connect-plugin-manager',
    version='0.1.0',
    description='Base Class for handling application startup.',
    long_description="not for now",
    keywords='ftrack',
    author='ftrack',
    author_email='support@ftrack.com',
    license='Apache License (2.0)',
    package_dir={'': 'source'},
    setup_requires=[
        'sphinx >= 1.8.5, < 4',
        'sphinx_rtd_theme >= 0.1.6, < 2',
        'lowdown >= 0.1.0, < 2',
    ],
    zip_safe=False,
    python_requires=">=3, <4"
)