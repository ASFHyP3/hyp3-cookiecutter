from pathlib import Path

from setuptools import find_packages, setup

readme = Path(__file__).parent / 'README.md'

setup(
    name='{{cookiecutter.package_name}}',
    use_scm_version=True,
    description='{{cookiecutter.short_description}}',
    long_description=readme.read_text(),
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
        'Programming Language :: Python :: 3.8',
       ],

    python_requires='~=3.8',

    install_requires=[
        'hyp3lib',
    ],

    extras_require={
        'develop': [
            'flake8',
            'flake8-import-order',
            'flake8-blind-except',
            'flake8-builtins',
            'pytest',
            'pytest-cov',
            'pytest-console-scripts',
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
