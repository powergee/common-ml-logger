import io
from os import name
from sys import version
from setuptools import setup, find_packages

def get_readme():
    with open("./README.md", "r") as fs:
        return fs.read()

setup(
    name='common_ml_logger',
    version='1.0',
    description='Log machine learning metrics to Comet, Neptune, local, etc with same interface',
    long_description=get_readme(),
    url='https://github.com/powergee/common-ml-logger',
    author='powergee',
    author_email='powergee101@gmail.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'comet_ml',
        'neptune_client',
        'tensorboardX'
    ],
    zip_safe=False
)