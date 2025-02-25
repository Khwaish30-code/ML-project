from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    Hyphen_e_dot = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)

    return requirements 
       

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Khwaish',
    author_email = 'khwaishkhandelwal30@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)

