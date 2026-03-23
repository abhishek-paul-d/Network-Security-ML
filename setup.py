'''
This setup.py file is an essential part if packaging and distributing python projects.
It is used by setuptools to define configuration of your project such as 
metadata dependencies and more

'''

from setuptools import find_packages,setup
from typing import List 

def get_requirements()->List[str]:
    """
    This Function will return list of requirements.txt
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ##Read lines from the file
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("My requirements.txt file not found")

    return requirement_list

setup(
    name="networksecurity",
    version="0.0.1",
    author="Abhishek",
    author_email="paulabhishek393@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
