import os

from setuptools import setup, find_namespace_packages

os.chdir(os.path.abspath(os.path.dirname(__file__)))

setup(
    name="marvelapi",
    version="0.0.1",
    description="Marvel api client and possible cli",
    long_description="{0}".format(open("README.rst").read()),
    author="Nathan Buckner",
    author_email="bucknerns@gmail.com",
    url="https://github.com/bucknerns/marvelapi",
    install_requires=["requests"],
    packages=find_namespace_packages("src"),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: Other/Proprietary License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only"],
    package_dir={"": "src"},
    entry_points={"console_scripts": [
        "staf = staf.runners.unittest.runner:entry_point"]})
