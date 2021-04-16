from setuptools import setup, find_packages

setup(
    name="project-name",
    version="3.7",
    package= find_packages(exclude="tests"),
    tests_requires=['unittest'],
    setup_requires=['pytest-runner'],
    install_require=['pandas']
)