from setuptools import setup, find_packages

setup(
    name='DarkCustom',
    version='0.1.0',
    packages=find_packages(exclude=['examples']), 
    author='vsp210',
    author_email='Tehno.Dark@yandex.ru',
    description='A library for custom colored input, print, confirm, progress bar, and spinner.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Dark-Tehno/DarkCustom',
)
