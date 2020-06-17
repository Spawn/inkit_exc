import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inkit_exc",
    version="0.0.2",
    author="Bohdan Vodopian",
    author_email="inkit@bohdan.com",
    description="Package for standardising HTTP errors for Inkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inkitio/inkit_exc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
