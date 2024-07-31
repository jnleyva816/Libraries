"""
setup.py used to setup packages and used to configure metadata
import setuptools 
Usage: 
python .\setup.py bdist_wheel sdisto 
"""

from setuptools import find_packages, setup 

with open("app/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name = "add_one",
    version = "1.0",
    description = "",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="",
    author="Joshua Leyva",
    author_email="joshleyva816@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",

    ],
    install_requires=[""],
    extras_require={
        "dev": [""]
    }
    ,
    python_requires=">=3.12",
)