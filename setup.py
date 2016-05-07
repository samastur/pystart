from setuptools import setup

DESCRIPTION = '''Dummy Python package demonstrating minimal package set up.'''

LONG_DESCRIPTION = DESCRIPTION

setup(
    #
    # PACKAGE DESCRIPTION
    #
    author="Marko Samastur",
    author_email="markos@gaivo.net",
    name='pystart',
    version='0.1',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url='https://github.com/samastur/pystart/',
    platforms=['OS Independent'],
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],

    #
    # PACKAGE SET UP
    #

    # Directory with package code that is also used as package's name in import
    # statements
    packages=['pystart'],

    # Dependencies (other Python packages required for this one to work)
    # install_requires=[
    #     'PyYAML>=3.11',
    # ],

    # Include data files found inside of this package directories which are
    # also specified in MANIFEST.in
    # include_package_data=True,

    # Functions to
    # entry_points={
    #     # Format: script_name=path_to_module:function_name
    #     'console_scripts': ['diet=pystart.cli:start'],
    # },

    # Can this project be safely installed and run from a ZIP file?
    # zip_safe=False
)
