#setup.py

from setuptools import setup, find_packages


setup(
    name = 'algoritmos_gen', #Nombre libreria
    version = '0.3', #Version inicial
    packages = find_packages(),
    description = "Esta es una libreria para implementar Algoritmos Genéticos",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown", #README
    author = "Adriana Osorio Kevin Romero",
    author_email = "osorioadriana99@gmail.com",
    url="https://github.com/AdrianaOsorio/algoritmos_gen",#URL del proyecto
    classifiers = [
        
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires = '>=3.10',
    install_requires=[
    ],

    )

    
    
