"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from typing import Any, Dict, Optional

from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    next(f)
    requirements = f.read().strip().split("\n")

packages = find_packages(exclude=["tests.*", "tests"])
version: Optional[Dict[str, Any]] = {}
with open("{}/__version__.py".format(packages[0])) as f:
    exec(f.read(), version)

setup(
    name="overlap_check",
    description="Check if two rectangles overlap",
    version=version["__version__"],
    url="https://xxx.com/",
    author="Mahdi Sadeghi",
    license="Mahdi Sadeghi",
    long_description=readme,
    packages=packages,
    package_data={
        "overlap_check/config": ["overlap_check/config/*.conf"]
    },
    include_package_data=True,
    #project_urls={"Source": "git@github.com:pppp"},
    install_requires=requirements,
)
