from codecs import open

from setuptools import setup, find_packages

from dj_impediments import __version__, __author__, __email__, __license__

setup(
    name="django-gddkia-impediments-on-roads",
    version=__version__,
    author=__author__,
    author_email=__email__,
    url='https://github.com/tomi77/django-gddkia-impediments-on-roads',
    description='Django client for gddkia-impediments-on-roads',
    long_description=open("README.rst").read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    license=__license__,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'django>=1.4',
        'gddkia-impediments-on-roads'
    ]
)