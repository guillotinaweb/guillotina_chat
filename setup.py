from setuptools import find_packages
from setuptools import setup


try:
    README = open('README.rst').read()
except IOError:
    README = None

setup(
    name='guillotina_chat',
    version="1.0.0",
    description='Guillotina server application python project',
    long_description=README,
    install_requires=[
        'guillotina<5',
        'guillotina_dbusers'
    ],
    author='',
    author_email='',
    url='',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    classifiers=[],
    entry_points={
    }
)
