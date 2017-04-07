from setuptools import setup, find_packages
import os
import re


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('bf1')

LONG_DESCRIPTION = open('README.rst').read()


setup(
    name="battlefield1-sdk",
    version=version,
    author="Alessandro De Angelis",
    author_email="alessandrodea22@gmail.com",
    description="Battlefield 1 sdk",
    long_description=LONG_DESCRIPTION,
    license="MIT",
    keywords="Battlefield 1 SDK",
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests', 'pyOpenSSL'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
