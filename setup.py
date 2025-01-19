from setuptools import setup, find_packages


setup(
    name='EcoAnalyzerPy',
    version='0.1',
    author= "Sohaib Khamlichi",
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'pandas',
        'geopandas']
    )
