import os

from setuptools import setup, find_packages

# readme = open('README.rst').read()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('dostuff', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']


install_requires = [
    'click==7.0',
]

packages = find_packages()

setup(
    name='dostuff',
    version=version,
    description=__doc__,
    keywords='dostuff',
    author='Miltiadis Alexis',
    author_email='alexmiltiadis@gmail.com',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'dostuff = dostuff.__main__:dostuff',
        ]
    },
    install_requires=install_requires,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
    ],
)