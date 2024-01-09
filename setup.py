from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Um facilitador para trabalhar com pickle files'
LONG_DESCRIPTION = 'sera que vai dar certo?'
# para criar o packege
#python3 setup.py sdist bdist_wheel
# dist é o q fazemos o upload
pip isntall twine
# twine upload dist/*

# Setting up
setup(
    name="picklefy",
    version=VERSION,
    author="Henrique Spencer)",
    author_email="<henriquespencer11@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)