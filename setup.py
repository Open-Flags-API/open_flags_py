from setuptools import setup, find_packages

setup(
    name='open_flags',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A package for retrieving flag SVGs',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/open-flags',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
