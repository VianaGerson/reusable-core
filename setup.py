import os
from setuptools import find_packages, setup
import glob
import pathlib
import subprocess

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open('requirements/requirements.txt') as f:
    install_requirements = f.readlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

name = 'reusable_core'
PO_FILES = name + '/locale/*/LC_MESSAGES/django.po'

# Compiled translations are not distributed via github (by default),
# so make them during setup


def create_mo_files():
    mo_files = []
    prefix = name

    for po_path in glob.glob(str(pathlib.Path() / PO_FILES)):
        mo = pathlib.Path(po_path.replace('.po', '.mo'))

        subprocess.run(['msgfmt', '-o', str(mo), po_path], check=True)
        mo_files.append(str(mo))

    return mo_files


setup(
    name='django-kong-core',
    version='0.0.0.1',
    license='BSD License',  # example license
    description='Django Kong Core',
    long_description=README,
    # url='https://www.example.com/',
    install_requires=install_requirements,
    author='Herlan Assis',
    author_email='herlan@evocorp.com.br',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    data_files=[(name, create_mo_files())],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
