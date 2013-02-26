#Setup.py for BrewMe virtual environment
from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
            name='BrewMe',
            version='0.0.1',
            Description='BrewMe website',
            packages=find_packages(),
            author='Paul Wyatt',
            install_requires="""
                Django==1.4.3
                ipython==0.13.1
                MySQL-python
                django_admin_bootstrapped
                South
                django-bootstrap-toolkit
                pil
            """,
            include_package_data=True,
        )
