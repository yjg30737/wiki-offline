from setuptools import setup, find_packages

setup(
    name='wiki-offline',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='convert Wikipedia html into txt which make it able to read offline',
    url='https://github.com/yjg30737/wiki-offline.git',
    install_requires=[
        'certifi',
        'urllib3',
        'bs4'
    ]
)