from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r')as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

setup(
    name="Network Security",
    version="0.0.1",
    author="Priyanka S A",
    author_email="priyankasa2092004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)