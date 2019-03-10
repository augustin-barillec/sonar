from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('requirements.txt') as f:
    REQUIREMENTS = f.read()

setup(
    name='sonar',
    version='0.0',
    long_description=README,
    install_requires=REQUIREMENTS,
    packages=find_packages())
