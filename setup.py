# TODO: But move to this when MVP is ready, and core logic are working good
from setuptools import setup, find_packages

setup(
    name='code_assistant',
    version='0.1.0',
    description='A Modular GenAI code assistant',
    author='NITS_cant',
    packages=find_packages(include=['core', 'core.*']),
    install_requires=[

    ],
    python_requres='>=3.8',
)