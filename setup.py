from pathlib import Path
from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Um facilitador para trabalhar com pickle files'
# para criar o packege
#python3 setup.py sdist bdist_wheel
# dist é o q fazemos o upload
# pip isntall twine
#twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --verbose --username __token__ --password <seu_token_de_api>
#twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --verbose --username __token__ --password pypi-AgEIcHlwaS5vcmcCJDA5OTAzZTUyLWVjY2EtNDVhNi1iOTQwLTNlYWQwN2ZiY2YwNAACKlszLCI5N2JhNGVkNi1kMWE2LTQwOGItYTdlZS0zY2NlMzIwNjY5ODAiXQAABiBik3Q8NWIg1gkgcu8UBJhRy3HfZchsLp9wWBuZluXrtQ

# python3 -m venv venv
# source venv/bin/activate
# Apagar: rm - env

# Setting uptwine upload dist/*
setup(
    name="picklefy",
    version=VERSION,
    author="Henrique Spencer)",
    author_email="<henriquespencer11@gmail.com>",
    description=DESCRIPTION,
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pickle'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
)