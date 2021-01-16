import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="khtube", # Replace with your own username
    version="0.9.22",
    author="Kodershub",
    author_email="furqan.ali9500@gmail.com",
    description="A youtube video downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KodersHub/khtube.git",
    packages=setuptools.find_packages(),
    install_requires=["youtube_dl"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)