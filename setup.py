from setuptools import setup

setup(
    name="LinkShort",
    version="0.1",
    description="The library for the LinkShort-api",
    license="MIT",
    author="Johannes Pour",
    url="https://github.com/Tch1b0/LinkShort-python-lib",
    author_email="Johannes@ben11.de",
    packages=["LinkShort"],
    package_requires=["requests==2.25.1"]
)