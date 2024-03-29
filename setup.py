import setuptools
from simufact_arc_reader import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Simufact_arc_reader",
    version=__version__,
    author="Léopold Le Roux",
    author_email="",
    description="A python reader for Simufact ARC file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lerouxl/Simufact_ARC_reader",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  
        "Operating System :: OS Independent",
    ),
    install_requires=['numpy>=1.2.0','polyscope>=1.2', 'xmltodict>=0.12.0']
)
