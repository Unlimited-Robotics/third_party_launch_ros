from setuptools import find_packages
from setuptools import setup

setup(
    name='launch',
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    author='Dirk Thomas',
    author_email='dthomas@osrfoundation.org',
    maintainer='Dirk Thomas',
    maintainer_email='dthomas@osrfoundation.org',
    url='https://github.com/ros2/launch',
    download_url='https://github.com/ros2/launch/releases',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Launch processes specified in launch files.',
    long_description=(
        'This package provides the ability to run multiple '
        'processes and react on individual processes exiting.'),
    license='Apache License, Version 2.0',
    test_suite='test',
    entry_points={
        'console_scripts': [
            'launch = launch.main:main',
        ],
    },
)