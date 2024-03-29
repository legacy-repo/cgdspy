#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from cgdspy import __version__

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests', 'pandas' ]

setup_requirements = ['pytest-runner', "isort"]

test_requirements = ['pytest', ]

setup(
    author="Jun Shang",
    author_email='shangjunv@163.com',
    maintainer="Choppy Team",
    maintainer_email="choppyteam@gmail.com",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python based API for accessing the Cancer Genomics Data Server (CGDS).",
    install_requires=requirements,
    license="GNU Affero General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cgdspy',
    name='cgdspy',
    packages=find_packages(include=['cgdspy']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/go-choppy/cgdspy',
    version=__version__,
    zip_safe=False,
)
