import os

from setuptools import find_packages, setup

_HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_HERE, 'README.md'), 'r') as f:
    long_desc = f.read()

setup(
    name='{{cookiecutter.package_name}}',
    use_scm_version=True,
    description='{{cookiecutter.short_description}}',
    long_description=long_desc,
    long_description_content_type='text/markdown',

    url='{{cookiecutter.public_url}}',

    author='ASF APD/Tools Team',
    author_email='uaf-asf-apd@alaska.edu',

    license='BSD',
    include_package_data=True,

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        ],

    python_requires='~=3.7',

    install_requires=[
        'hyp3lib',
        'hyp3proclib',
        'importlib_metadata',
    ],

    extras_require={
        'develop': [
            'pytest',
            'pytest-cov',
            'pytest-console-scripts',
            'tox',
            'tox-conda',
        ]
    },

    packages=find_packages(),

    entry_points={'console_scripts': [
            '{{cookiecutter.package_name}} = {{cookiecutter.package_name}}.__main__:main',
            '{{cookiecutter.process_name}} = {{cookiecutter.package_name}}.process:main',
        ]
    },

    zip_safe=False,
)
