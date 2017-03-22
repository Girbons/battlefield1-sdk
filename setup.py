from setuptools import setup, find_packages


setup(
    name="battlefield1-sdk",
    version="0.1",
    description="Battlefield 1 SDK python",
    long_description=open('README.rst').read(),
    author="Alessandro De Angelis",
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyOpenSSL',
        'six'
    ]
)
