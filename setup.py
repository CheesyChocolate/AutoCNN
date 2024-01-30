#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="auto_cnn",
    version="1.0",
    author="Suren Lockwood",
    author_email="dev@behnamlal.xyz",
    description="Automatically designing CNN architectures using Genetic Algorithm for Image Classification "
                "implementation",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/CheesyChocolate//AutoCNN",
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Image Processing'
    ],
    python_requires='>=3.6',
    install_requires=[
        'tensorflow>=2.0.0'
        'numpy>=1.22.0',
        ],
)
