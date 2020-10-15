#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


package_name = 'project_sketch'


def get_version():
    import ast

    def parse_version(f):
        for line in f:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s

    for i in [package_name + '/__init__.py', package_name + '.py']:
        try:
            with open(i, 'r') as f:
                return parse_version(f)
        except IOError:
            pass


def get_requires():
    try:
        with open('requirements.txt', 'r') as f:
            requires = [i.split(' ')[0] for i in map(lambda x: x.strip(), f.readlines())
                        if i and i[0] not in ['#', '-']]
        return requires
    except IOError:
        return []


def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return ''


setup(
    # license='License :: OSI Approved :: MIT License',
    name=package_name,
    version=get_version(),
    author='',
    author_email='',
    description='',
    url='',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=[
        'project_sketch',
        'project_sketch/_module'
    ],
    # Or use (make sure find_packages is imported from setuptools):
    #packages=find_packages(),
    # Or if it's a single file package
    #py_modules=[package_name],
    install_requires=get_requires(),
    # including data files
    #include_package_data=True,
    #package_data={},
    # entry_points={'console_scripts': ['foo = package.module:main_func']}
)
