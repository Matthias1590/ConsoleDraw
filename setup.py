from setuptools import setup


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="consoledraw",
    version="2.3.8",
    description="A python module to update the console without flashing.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matthias1590/ConsoleDraw",
    author="Matthias Wijnsma",
    author_email="matthiasx95@gmail.com",
    license="MIT",
    python_requires=">=3.6",
    packages=["consoledraw"]
)
