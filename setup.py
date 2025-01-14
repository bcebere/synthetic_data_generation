"""
    Setup file for synthesis.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.2.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup

def find_version() -> str:
    return "0.1.3"

if __name__ == "__main__":
    try:
        setup(version=find_version())
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
