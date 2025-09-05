## It is used to make whole ml project into an package so that anywhere and anybody can use it
from setuptools import find_packages, setup
from typing import List

const = "-e ."
def get_requirements(file_path:str)->List[str]:
    # This function will return list of requirements
    requirements = []
    with open(file_path) as fp:
        requirements=fp.readlines()
        requirements = [r.replace("\n", "")for r in requirements]
        
        if const in requirements:
            requirements.remove(const)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Dinesh',
    author_email='dinu08642@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    
)