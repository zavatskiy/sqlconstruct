from os.path import join, dirname
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open(join(dirname(__file__), 'README.rst')) as f:
    README = f.read()


setup(
    name='SQLConstruct',
    version='0.1',
    description='Functional approach to query database using SQLAlchemy',
    long_description=README,
    author='Vladimir Magamedov',
    author_email='vladimir@magamedov.com',
    url='http://github.com/vmagamedov/sqlconstruct',
    license='BSD',
    install_requires=['SQLAlchemy>=0.7'],
    py_modules=['sqlconstruct'],
)
