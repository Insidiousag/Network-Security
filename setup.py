'''
setup.py is essential for packaging and distributing Python projects. 
It defines the metadata and dependencies of the project, allowing it to be easily installed and shared. 
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    Reads the requirements.txt file and returns a list of dependencies.
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                #ignore empty line and -e . which is for editable install
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

print(get_requirements())


setup(
    name='NetworkSecurity',
    author='Aman Gupta',
    version='0.1.0',
    packages=find_packages(),
    author_email="workmanit27@gmail.com",
    install_requires=get_requirements(),
)