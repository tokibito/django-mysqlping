import os
from setuptools import setup, find_packages

current_dir = os.path.dirname(os.path.abspath(__file__))


def read(filename):
    fullpath = os.path.join(current_dir, filename)
    try:
        with open(fullpath) as f:
            return f.read()
    except Exception:
        return ""


setup(
    name='django-mysqlping',
    version='0.1.1',
    description="Ping to MySQL in Django middleware.",
    long_description=read('README.rst'),
    packages=find_packages(),
    author='Shinya Okano',
    author_email='tokibito@gmail.com',
    url='https://github.com/tokibito/django-mysqlping',
    install_requires=['Django>=1.11'],
    extras_require={
        'develop': [
            'pytest', 'flake8', 'pytest-django',
            'pytest-pythonpath', 'tox', 'wheel', 'twine'
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ])
