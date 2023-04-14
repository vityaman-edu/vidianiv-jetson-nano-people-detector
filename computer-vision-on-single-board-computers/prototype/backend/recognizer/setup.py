#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='vidianiv_people_recognizer',
    version='0.0.1',
    description='A package with people recognizer for vidianiv project.',
    long_description=long_description,

    author='Victor Smirnov',
    author_email='vityaman.dev@yandex.ru',
    url='https://gitlab.se.ifmo.ru/vidianiv/projects',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.10",
    install_requires=[
        "numpy==1.24.2",
        "opencv-python==4.7.0.72"
    ],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)
