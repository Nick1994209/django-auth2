import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-auth2',
    version='0.1',
    packages=['auth2'],
    description='Login, Registration and Resset password, ActivateUser',
    long_description=README,
    author='Nikita Korolkov',
    author_email='nick1994209@gmail.com',
    url='https://github.com/yourname/django-myapp/',
    license='MIT',
    install_requires=[
        'Django>=1.10',
    ]
)
