import os
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "othellotk",
    version = "0.1.1",
    packages = ["othellotk"],

    entry_points={
        'gui_scripts': [
            'othellotk = othellotk.othellotk:main',
        ]
    },

    # metadata for upload to PyPI
    author = "John Cheetham",
    author_email = "kaama12@yahoo.co.uk",
    description = "Edax gui to play Othello against the Edax engine",
    license = "GPLv3+",
    keywords = "othello edax tkinter",
    url = "http://www.johncheetham.com/projects/othellotk/",
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: X11 Applications",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Board Games",
    ],
)
