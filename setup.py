"""
Setup file for headLineStyle.
"""
import setuptools

setuptools.setup(
    name="headline_style",  # This is the name of the package
    version="1.0.0",  # The initial release version
    author="Vinod Baste",  # Full name of the author
    url="https://github.com/vinodbaste/python_headline_style",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.7',  # Minimum version requirement of the package
    py_modules=["headLineStyle"],  # Name of the python package
    install_requires=["regex >=2020.4.4"]  # Install other dependencies if any
)
