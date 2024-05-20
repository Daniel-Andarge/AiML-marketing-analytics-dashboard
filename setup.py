import setuptools
from setuptools import find_packages, setup
from pkg_resources import parse_requirements

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = parse_requirements('requirements.txt')

setuptools.setup (
    name='src',
    packages=find_packages(),
    version='0.1.0',
    author='Daniel Andarge',
    version="0.1.0",
    author_email="andargedaniel90@gmail.com",
    description='The Marketing Analytics Dashboard project is a comprehensive solution designed to monitor and evaluate the efficiency of marketing ads for a tech-savvy bank in Ethiopia.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-package",
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[str(req) for req in requirements],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)