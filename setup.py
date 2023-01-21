"""
Setup file for headLineStyle.
"""

try:
    import pypandoc

    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

import setuptools

setuptools.setup(
    name="headline_style",  # This is the name of the package
    version="1.0.2",  # The initial release version
    author="Vinod Baste",  # Full name of the author
    url="https://github.com/vinodbaste/python_headline_style",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    readme="README.md",
    description="About This filter changes a given text to Title Caps, and attempts to be clever about SMALL words "
                "like a/an/the in the input. The list of SMALL words which are not capped comes from the New York "
                "Times Manual of Style, plus some others like 'vs' and 'v'.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.7',  # Minimum version requirement of the package
    py_modules=["headline_style"],  # Name of the python package
    install_requires=["regex >=2020.4.4"],  # Install other dependencies if any
    download_url="https://github.com/vinodbaste/python_headline_style/archive/refs/heads/main.zip"
)
