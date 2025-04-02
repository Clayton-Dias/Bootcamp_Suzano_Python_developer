from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Clayton",
    description="Project for Image Processing using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="mhttps://github.com/Clayton-Dias/Bootcamp_Suzano_Python_developer/tree/main",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)