#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    description="Project Kidu",
    author="Gokul P V",
    author_email="25975535+gokul-pv@users.noreply.github.com",
    url="https://github.com/Project-Kidu/code-repo",
    install_requires=["pytorch-lightning", "hydra-core"],
    packages=find_packages(),
    include_package_data=True,
)
