from setuptools import find_packages,setup
from typing import List


HYPEN_DOT_E = '-e .'
def get_requirements(path:str)-> List[str]:
    with open(path,'r') as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n', "") for req in requirement ]
        if HYPEN_DOT_E in requirement:
            requirement.remove(HYPEN_DOT_E)
    return requirement

setup(
    name='CHAT APPLICATION',
    version='0.0.1',
    author='Mahavir Rajpurohit',
    author_email='mrajpurohit1912@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requriments.txt')
)