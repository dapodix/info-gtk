import os
from setuptools import setup, find_packages

__version__ = ""
packages = find_packages(exclude=["tests*"])

fn = os.path.join("info_gtk", "version.py")
with open(fn) as fh:
    code = compile(fh.read(), fn, "exec")
    exec(code)


setup(
    name="info-gtk",
    version=__version__,
    author="hexatester",
    license="GPLv3",
    url="https://github.com/dapodix/info-gtk",
    keywords="dapodik info-gtk kemdikbud",
    description="Exporter-scraper info-gtk",
    packages=packages,
    package_data={"info_gtk": ["template/*.xlsx"]},
    install_requires=[
        "python",
        "requests",
        "json5",
        "attrs",
        "bs4",
        "openpyxl",
        "click",
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={"console_scripts": ["info-gtk=info_gtk.infogtk:main"]},
)
