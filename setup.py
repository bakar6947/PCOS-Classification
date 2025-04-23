from setuptools import setup, find_packages
from typing import List




HYPHON_E = '-e .'
# Get all packages form file
def get_packages(file_name:str)->List[str]:

    packages = []
    with open(file_name) as file:
        packages = file.readlines()
        
        # Handle \n
        packages = [pkg.replace('\n', '') for pkg in packages]

        # Remove -e .
        if HYPHON_E in packages:
            packages.remove(HYPHON_E)
        
        return packages
    



# Configure Project Setup
setup(
    name='Polycystic Ovary Syndrome (PCOS) Classification',
    version='0.1.0',
    author='Abu Bakar',

    packages=find_packages(),
    install_requires=get_packages('requirements.txt')
)