import os
from glob import glob
from setuptools import setup

exec(open("shout/version.py").read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="shout",
    version=__version__,
    description="Render SMILES into 3D video",
    author="Andrew White, Chase Thomas, Tim Hansan",
    author_email="andrew.white@rochester.edu",
    url="https://github.com/whitead/shout",
    license="MIT",
    packages=["shout"],
    install_requires=[
        "zmq",
        "click"
    ],
    entry_points="""
        [console_scripts]
        shout=shout.main:transcribe
            """,
    package_data={"shout": ["vmd/*.vmd"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
)
