import os
import re

from setuptools import setup, find_packages


VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*args):
    """Reads complete file contents."""
    return open(os.path.join(HERE, *args)).read()


def get_version():
    """Reads the version from this module."""
    init = read('src', '__init__.py')
    return VERSION_RE.search(init).group(1)


def get_requirements():
    """Reads the requirements file."""
    requirements = read("requirements.txt")
    return list(requirements.strip().splitlines())


setup(
    name='ac-dencryption-lib',
    version=get_version(),
    url='https://github.com/shinsaka/amazon-connect-dencryption-lib',
    author='shinsaka',
    author_email='shinx1265@gmail.com',
    maintainer='shinsaka',
    maintainer_email='shinx1265@gmail.com',
    description='Amazon Connect Dencryption Library for Python',
    long_description=read('README.rst'),
    packages=find_packages(),
    install_requires=get_requirements(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
)

